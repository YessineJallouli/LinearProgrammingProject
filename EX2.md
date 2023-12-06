![image-20231206020502602](/home/yessine/.config/Typora/typora-user-images/image-20231206020502602.png)

#### Les paramètres à entrer : 

**$c_{i}$** : demande de $i$ème mois

**nbOuv** : nombre d'ouvrier disposé

**salaire** : salaire d'un ouvrier

**nbH** : nombre d'heure travaillé par un ouvrier pendant un mois

**nbSp** : nombre d'heures supplementaire par mois 

**prixSup** : prix d'une heure supplementaire

**tmpCh**  : temps pour faire une paire de chaussure

**rec** : Frais du recrutement

**lic**  : Frais du licenciement

#### Les variables de décisions : On définit les variables suivantes : 

$x_{i} :$ Le nombre d'ouvrier à recruter le ième mois 

$y_{i} : $ Le nombre d'ouvrier à licencier le ième mois

$z_{i}$ : La somme de nombre d'heures supplémentaire à travailler le ième mois

#### Fonction Objective :  On cherche à minimiser le coût :

$$
\begin{align*}
& \sum_{i=1}^{4} \left[x_{i}.rec+y_{i}.lic+z_{i}.prixSup + \left( nbOuv +\sum_{j=1}^{i} x_{j}-y_{j}\right).salaire\right] \\
\end{align*}
$$

$i = 1 :$
$$
\begin{align*}
&  x_{1}.rec+y_{1}.lic+z_{1}.prixSup + \left( nbOuv + x_{1}-y_{1}\right).salaire 
\end{align*}
$$
$i = 2 :$
$$
\begin{align*}
&  x_{2}.rec+y_{2}.lic+z_{2}.prixSup + \left( nbOuv + x_{1}+x_{2}-y_{1}-y_{2}\right).salaire 
\end{align*}
$$
$i = 3:$
$$
\begin{align*}
&  x_{3}.rec+y_{3}.lic+z_{3}.prixSup + \left( nbOuv + x_{1}+x_{2}+x_{3}-y_{1}-y_{2}-y_{3}\right).salaire 
\end{align*}
$$
$i = 4:$
$$
\begin{align*}
&  x_{4}.rec+y_{4}.lic+z_{4}.prixSup + \left( nbOuv + x_{1}+x_{2}+x_{3}+x_{4}-y_{1}-y_{2}-y_{3}-y_{4}\right).salaire 
\end{align*}
$$
**Coefficients : **

$x_{1} : rec+4.salaire$

$x_{2} : rec+3.salaire$

$x_{3} : rec+2.salaire$

$x_{4} : rec+salaire$

$y_{1} : lic-4.salaire$

$y_{2} : lic-3.salaire$

$y_{3} : lic-2.salaire$

$y_{4} : lic-salaire$

$z_{i} : prixSup$

**Fonction objectif : (Minimiser cette fonction)**
$$
\boxed{
\begin{align*}
&(rec+4.salaire).x_{1} + (rec+3.salaire).x_{2} + (rec+2.salaire).x_{3}+(rec+salaire).x_{4} + (lic-4.salaire).y_{1} \\ 
&+(lic-3.salaire).y_{2}+ (lic-2.salaire).y_{3} + (lic-salaire).y_{4} + z_{1}.prixSup + z_{2}.prixSup + z_{3}.prixSup + z_{4}.prixSup
\end{align*}
}
$$

#### Contraintes : 

**On doit trouver des ouvriers qui peuvent faire des heures supplementaires** 
$$
c2 : \left( nbOuvrier +\sum_{j=1}^{i} x_{j}-y_{j}\right).nbSup \ge z_{i} \ pour \ tout \ i
$$
$$
\boxed{
\begin{align*}
& x_{1}.nbSp-y_{1}.nbSp-z_{1} \ge -nbOuv.nbSp \\
&x_{1}.nbSp+x_{2}.nbSp-y_{1}.nbSp-y_{2}.nbSp-z_{2} \ge -nbOuv.nbSp \\
&x_{1}.nbSp+x_{2}.nbSp+x_{3}.nbSp-y_{1}.nbSp-y_{2}.nbSp-y_3{}.nbSp-z_{3}  \ge -nbOuv.nbSp \\
&x_{1}.nbSp+x_{2}.nbSp+x_{3}.nbSp+x_{4}.nbSp-y_{1}.nbSp-y_{2}.nbSp-y_3.nbSp-y_{4}.nbSp-z_{4}  \ge -nbOuv.nbSp \\
\end{align*}
}
$$

**Les variables doivent être positifs**
$$
\boxed{
c3 : (x_{i}, y_{i}, z_{i} \ge 0)
}
$$
**On peut satisfaire les demandes pendant chaque mois** 
$$
c4 : \left[ \frac{\left( nbOuv +\sum_{j=1}^{i} x_{j}-y_{j}\right).nbH +z_{i}}{tmpCh} \right]  \ge c_{i}
$$

$$
\Longrightarrow\left( nbOuv +\sum_{j=1}^{i} x_{j}-y_{j}\right).nbH +z_{i} \ge c_{i}.tmpCh
$$

$$
\boxed{
\begin{align*}
& x_{1}.nbH-y_{1}.nbH+z_{1} \ge -nbOuv.nbH+c_{1}.tmpCh \\
& x_{1}.nbH+x_{2}.nbH-y_{1}.nbH-y_{2}.nbH+z_{2} \ge -nbOuv.nbH+c_{2}.tmpCh \\
& x_{1}.nbH+x_{2}.nbH+x_{3}.nbH-y_{1}.nbH-y_{2}.nbH-y_{3}.nbH+z_{3} \ge -nbOuv.nbH+c_{3}.tmpCh \\
& x_{1}.nbH+x_{2}.nbH+x_{3}.nbH+x_{4}.nbH-y_{1}.nbH-y_{2}.nbH-y_{3}.nbH-y_{4}.nbH+z_{4} \ge -nbOuv.nbH+c_{4}.tmpCh \\
\end{align*}
}
$$