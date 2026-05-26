# Power of Friendship

Problem Setter: [Syed Rifat Raiyan](https://codeforces.com/profile/Starscream-11813)

Estimated Difficulty: 1300

Tag(s): Geometry

<details>
<summary>Hint</summary>

Scale the problem down to $2D$ and then scale the observations back up to $3D$.

</details>

<details>
<summary>Solution</summary>

Ignoring the details about atoms and BCC lattices, the problem simply asks for the volume of the shape consisting of all points that are closer to the center of a cube than to any corner (vertex) of that cube, while still lying inside that cube.

![Cell 3D](./img/Cell-3D.png 'The domain is the set of points that are inside the cube and closer to the blue atom than any of the red atoms.')

_In problem solving, if a problem feels too complex, it is often helpful to first solve an easier version of it._ Here, the geometry in $3$ dimensions is difficult to visualize immediately, so you can first scale the problem down to $2$ dimensions and look for observations.

---

In $2D$, imagine a square instead of a cube. The question becomes:

> What is the area of all points inside the square that are closer to the center than to any corner?

Draw the square and mark its center.

![Cell 2D](./img/Cell-2D.png '2D Cell')

Now connect the center to one of the corners. The boundary between points closer to the center and points closer to that corner is the perpendicular bisector of that segment.

Doing this for all four corners gives four bisectors.

![Bisector 2D](./img/Bisector-2D.png '2D Bisector')

A useful observation appears immediately: each bisector intersects the square exactly at the midpoint of an edge.

So the domain of the center is simply the diamond formed by joining the four edge midpoints.

![Domain 2D](./img/Domain-2D.png '2D Domain')

If the side length of the unit square is $a$, the area of the domain, $\displaystyle A_{domain} = \frac{a^2}{2}$

---

Now, formalize the original problem, define a $3D$ Cartesian coordinate system so that the **center** of the cube is at $(0,0,0)$ and the $8$ **vertices** are $\displaystyle (\pm \frac{a}{2}, \pm \frac{a}{2}, \pm \frac{a}{2})$, where $a = \dfrac{p}{q}$ is the side length of the cube.

The $6$ faces of the cube are $\displaystyle x = \pm \frac{a}{2}, y = \pm \frac{a}{2}, z = \pm \frac{a}{2}$.

A point $(x, y, z)$ is inside the domain if:

- The point is inside the cube:  
  $\displaystyle \lvert x \rvert < \frac{a}{2}, \lvert y \rvert < \frac{a}{2}, \lvert z \rvert < \frac{a}{2}$
- The point is closer to the center than any vertex:  
  $\displaystyle \sqrt{x^2 + y^2 + z^2} < (\lvert x \rvert - \frac{a}{2})^2 + (\lvert y \rvert - \frac{a}{2})^2 + (\lvert z \rvert - \frac{a}{2})^2$

Simplifying the second condition yields $\displaystyle \lvert x \rvert + \lvert y \rvert + \lvert z \rvert \le \frac{3a}{4}$

---

The same way you used perpendicular bisector lines to determine the domain in $2D$, you can do the same thing in $3D$. For each vertex of the cube, consider the segment connecting that vertex to the center. The set of points that are equally distant from the center and that vertex forms a perpendicular bisector plane. Since the cube has $8$ vertices, this gives $8$ bisector planes in total.

![Bisector 3D](./img/Bisector-3D.png "Each green bisector plane separates the entire 3D space into two half-spaces: one side is closer to the center, and the other side is closer to a vertex. The domain you want is must lie on the 'center side' of all eight planes at once.")

Conceptually the idea looks identical: in $2D$, the domain is the intersection of four half-planes; in $3D$, it becomes the intersection of eight half-spaces. Or is it?

In $2D$, the bisectors immediately determined the shape of the domain, because each bisector met the boundary of the square at a single point - the midpoint of an edge. Once those four points were known, the shape was clear. You need to check whether the same thing happens in $3D$.

Check if the condition $\displaystyle \lvert x \rvert + \lvert y \rvert + \lvert z \rvert \le \frac{3a}{4}$ is sufficient.

Take the face $\displaystyle x = \frac{a}{2}$.

Check its intersection with the bisectors by substituting into the inequality:

$\displaystyle \frac{a}{2} + \lvert y \rvert + \lvert z \rvert \le \frac{3a}{4} \implies \lvert y \rvert + \lvert z \rvert \le \frac{a}{4}$

This is exactly a square on that face, rotated $45^\circ$. The same happens on all six faces.

![Intersection 3D](./img/Intersection-3D.png 'The green bisector planes intersect not only with each other, but also with the face of the cube, creating the yellow intersection squares on each face.')

Unfortunately, this makes the geometry more complicated in $3D$. A bisector plane does not intersect a face of the cube at a single point. Instead, it cuts through the face along an entire line. When several bisector planes interact, the boundary they create on a face is not just a vertex but a full $2D$ shape.  
So, unlike the $2D$ case, knowing the bisector planes alone is not enough to determine the domain. The faces of the cube now matter!

---

The shape of the domain is actually a famous solid in crystallography called a **Wigner–Seitz cell**.  
Trying to compute its volume directly is possible, but difficult.

A cleaner strategy is to compute the volume of the region outside the domain and subtract it from the volume of the unit cube.

Define the **negative region** as all points that are:

- inside the cube,
- but outside the center's domain.

Then, $\boxed{V_{domain} = a^3 - V_{negative}}$

---

You can go to the 2D version of the problem and solve it using the same technique.

![Negative 2D](./img/Negative-2D.png 'The negative region consists of the 4 red right triangles - one for each corner.')

Area of unit square $= a^2$

Area of each triangle in corner, $\displaystyle A_{triangle} = \frac{1}{2} \times \frac{a}{2} \times \frac{a}{2} = \times \frac{a^2}{8}$

There are $4$ triangles for the $4$ vertices of the square.

So, $\displaystyle A_{negative} = 4 \times \frac{a^2}{8} = \frac{a^2}{2}$

So, $\displaystyle A_{domain} = a^2 - \frac{a^2}{2} = \frac{a^2}{2}$

---

To understand the negative region, focus on one corner of the cube, for example $\displaystyle (\frac{a}{2}, \frac{a}{2}, \frac{a}{2})$.

Imagine slicing off this corner using the perpendicular bisector plane between the corner and the center. This creates one flat polygonal boundary.

The corner is incident on three faces of the cube: $\displaystyle x = \frac{a}{2}, y = \frac{a}{2}, z = \frac{a}{2}$.

The bisector plane intersects each of these faces. That gives three line segments.  
At the same time, this plane also meets the three neighboring bisector planes coming from the adjacent corners. That creates three more line segments.  
Together, these six segments connect into one closed shape, which is a **hexagon**.

Now think about the region between the corner and this hexagon. That is a pyramid with a hexagonal base. So each corner contributes one hexagonal pyramid pointing inward toward the corner.

![Hexagonal Pyramid](./img/Pyramid.png 'Each bisector plane intersects three neighboring faces and three neighboring bisectors, creating a hexagon. For each vertex, the negative region contains a hexagonal pyramid where the base is the mentioned hexagon and the apex is the vertex itself. The green solid shown is one of those pyramids.')

---

At this point it may look like the pyramid completely fills the negative region near that corner. But if you inspect one edge of the cube more carefully, there is still some leftover space.

For example, take the edge shared by $\displaystyle x = \frac{a}{2}, y = \frac{a}{2}$. The hexagonal pyramid does not extend all the way into this edge.

![Tetrahedron](./img/Tetrahedron.png 'A small wedge remains trapped between the pyramid, and the two faces meeting at that edge. The leftover region is shown in pink.')

On each face, the leftover region forms a triangle. These triangular slices extend inward and meet in space. That produces a triangular pyramid -- a tetrahedron.

The same thing happens along each of the three edges incident on the corner.  
So besides the hexagonal pyramid in the middle, each corner also contributes three tetrahedrons tucked into the edges to the negative region.

---

![Negative Region](./img/Negative-3D.png 'To the negative region, each vertex contributes one hexagonal pyramid (green) and three tetrahedrons (pink) that are independent.')

Every corner of the cube has exactly the same geometry.  
For every corner, the negative region contains $1$ hexagonal pyramid and $3$ tetrahedrons.  
Since the cube has $8$ vertices, the negative region consists of $8$ hexagonal pyramids and $24$ tetrahedrons.

So, $\boxed{V_{domain} = a^3 - 8 V_{pyramid} - 24 V_{tetrahedron}}$

---

Start with the hexagonal pyramid.

![Hexagonal Pyramid](./img/Pyramid.png 'The base of the pyramid is a regular hexagon and the apex is the vertex of the cube.')

Notice that it's base is a regular hexagon where the length of each side is $\displaystyle \sqrt{\left(\frac{a}{4}\right)^2 + \left(\frac{a}{4}\right)^2} = \frac{a}{\sqrt{8}}$.

Area of the base of the pyramid $\displaystyle 6 \times \left[\frac{\sqrt{3}}{4} \times \left(\frac{a}{\sqrt{8}}\right)^2 \right] = \frac{6 \sqrt{3} a^2}{32}$

Now, the apex is the corner itself.  
The base lies on the bisector plane, which is halfway between the center and that corner.  
The distance from the center to a vertex is half the cube diagonal: $\displaystyle \frac{\sqrt{3}a}{2}$  
The pyramid height is half of that which is $\displaystyle \frac{\sqrt{3}a}{4}$

So, $\displaystyle \boxed{V_{pyramid} = \frac{1}{3} \times \frac{6 \sqrt{3} a^2}{32} \times \frac{\sqrt{3}a}{4} = \frac{6 a^3}{128}}$

---

Next look at a tetrahedron.

![Tetrahedron](./img/Tetrahedron.png 'The base of the tetrahedron (inside the unit cube) is a isosceles right triangle and the height is half the side length of the cube.')

The tetrahedron sits along one edge of the cube. Its base is inside the cube and forms a right triangle with the two legs on two adjacent faces of the cube.

The length of each leg $\displaystyle = \frac{a}{4}$  
So, the base area of the tetrahedron $\displaystyle = \frac{1}{2} \times \frac{a}{4} \times \frac{a}{4} = \frac{a^2}{32}$

The height of the tetrahedron is half the side length of the cube, which is $\dfrac{a}{2}$.

So, $\displaystyle \boxed{V_{tetrahedron} = \frac{1}{3} \times \frac{a^2}{32} \times \frac{a}{2} = \frac{a^3}{192}}$

---

Finally, $\displaystyle \boxed{V_{domain} = a^3 - 8 \times \frac{6 a^3}{128} - 24 \times \frac{a^3}{192} = \frac{a^3}{2}}$

</details>

<details>
<summary>Alternate Solution</summary>

Unlike the first solution, don't ignore the details. Think about the atoms and the lattice, and think outside the box (literally)!

Notice that a center atom has $8$ neighboring atoms, all at the same distance. But the same is also true for every corner atom.

**So whether an atom appears as a 'center atom' or a 'corner atom' depends only on which atom you are focusing at.**

This means every atom has its own domain, and every point in the lattice belongs to exactly one atom's domain (unless it lies on a border between multiple domains).

Because all atoms are symmetric, every domain has the same size.

Let that common area or volume be $\displaystyle d$.

---

Now start with the $2D$ version.

Each unit square contains:

- one full center atom,
- and four corner atoms.

Each corner atom is shared equally between four adjacent squares. So inside one square, one corner atom contributes $\displaystyle \frac{d}{4}$.

The unit square consists of one fourth of the domains of four corner atoms and the entire domain of the center atom.

Formally, $\displaystyle d + 4 \times \frac{d}{4} = a^2$

$\displaystyle \implies d + d = a^2$

$\displaystyle \implies 2d = a^2$

$\displaystyle \therefore d = \frac{a^2}{2}$.

---

Unlike the previous solutions, this logic translates seamlessly to $3D$!

Each unit cube contains:

- one full center atom,
- and eight corner atoms.

Each corner atom is shared equally between eight neighboring cubes. So inside one cube, one corner atom contributes $\displaystyle \frac{d}{8}$.

The unit cube consists of one eigth of the domains of eight corner atoms and the entire domain of the center atom.

Formally, $\displaystyle d + 8 \times \frac{d}{8} = a^3$

$\displaystyle \implies d + d = a^3$

$\displaystyle \implies 2d = a^3$

$\displaystyle \boxed{\therefore d=\frac{a^3}{2}}$.

</details>

<details>
<summary>Code</summary>

```cpp
#include <bits/stdc++.h>
using namespace std;

#define fastio ios_base::sync_with_stdio(0); cin.tie(0)
using LL = long long;



void pre()
{
    fastio;

    cout << fixed << setprecision(7);
}

void solve(int tc)
{
    int p, q;
    long double a;

    cin >> p >> q;
    a = 1.0L * p / q;

    cout << a * a * a / 2;
}

int main()
{
    pre();

    int tc, tt = 1;
    cin >> tt;

    for(tc = 1; tc <= tt; tc++)
    {
        // cout << "Case " << tc << ": ";
        solve(tc);
        cout << '\n';
    }

    return 0;
}
```

</details>

<details>
<summary>Trivia</summary>

The problem is taken from the final exam of [Assassination Classroom, Season 2, Episode 12](https://www.youtube.com/watch?v=IsTMsq5EVbU), introduced to the setter by [Rafio](https://codeforces.com/profile/Rafio).

This is a beautiful episode where a math problem is connected directly to the themes of a story. Although Assassination Classroom is a quite an absurd anime in general, the context of this problem can be easily explained.

**SPOILER ALERT!**

The problem appears in the final exam of Kunugigaoka Junior High School. Among all the students, the only ones who have the chance of solving this problem are Asano and Karma.

Asano, the principal's son and the top student of Class A, was raised under constant pressure to become perfect. His entire life revolves around competition, discipline, and proving himself superior to others. Determined to prove his father wrong, when Asano approaches the problem, he sees the cube as a battlefield. He imagines each corner of the room as an enemy. To create his own domain, he draws eight bisector planes and claims the central region for himself. From there, he starts calculating the volume of the remaining region using careful geometry. He was just about to finish the problem when time ran out.

Karma, on the other hand, approaches the problem in a completely different way.  
At the beginning of the series, Karma was an extremely talented but overconfident student. During the midterm exams, he underestimated both the exam and the people around him, which led to a humiliating result. But throughout his adventures with his classmates and Koro-sensei, he has become humble and learned to appreciate others around him. That growth is reflected perfectly in the way he solves this problem.

Karma realizes that there is a world outside his unit cube. He thinks of the cube not as a battlefield, but as a representation of relationships. In everyone's life, they themselves are the center, while the people around them are the corners. But just as his friends are corners in his own life, he is also a corner in theirs. Instead of treating the corners as enemies like Asano does, Karma treats them as equals. This immediately reveals the symmetry of the construction, allowing him to avoid all the tedious geometric calculations entirely.

Within the themes of the story, Karma quite literally solves a math problem using the power of friendship.

</details>
