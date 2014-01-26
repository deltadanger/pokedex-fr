package fr.pokedex;

import java.util.HashMap;

public class ReceiveTypeTable {
    @SuppressWarnings("serial")
    public static HashMap<Type, HashMap<Type, Weakness>> table = new HashMap<Type, HashMap<Type,Weakness>>() {{
        
        this.put(Type.NONE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});
        
        this.put(Type.ACIER, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.STRONG);
            this.put(Type.COMBAT, Weakness.WEAK);
            this.put(Type.DRAGON, Weakness.STRONG);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.STRONG);
            this.put(Type.FEU, Weakness.WEAK);
            this.put(Type.GLACE, Weakness.STRONG);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.STRONG);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.IGNORE);
            this.put(Type.PSY, Weakness.STRONG);
            this.put(Type.ROCHE, Weakness.STRONG);
            this.put(Type.SOL, Weakness.WEAK);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.STRONG);
        }});

        this.put(Type.COMBAT, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.WEAK);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.WEAK);
            this.put(Type.ROCHE, Weakness.STRONG);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.STRONG);
            this.put(Type.VOL, Weakness.WEAK);
        }});

        this.put(Type.DRAGON, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.WEAK);
            this.put(Type.EAU, Weakness.STRONG);
            this.put(Type.ELECTRIQUE, Weakness.STRONG);
            this.put(Type.FEE, Weakness.WEAK);
            this.put(Type.FEU, Weakness.STRONG);
            this.put(Type.GLACE, Weakness.WEAK);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.EAU, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.STRONG);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.STRONG);
            this.put(Type.ELECTRIQUE, Weakness.WEAK);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.STRONG);
            this.put(Type.GLACE, Weakness.STRONG);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.WEAK);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.ELECTRIQUE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.STRONG);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.STRONG);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.WEAK);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.STRONG);
        }});

        this.put(Type.FEE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.WEAK);
            this.put(Type.COMBAT, Weakness.STRONG);
            this.put(Type.DRAGON, Weakness.IGNORE);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.WEAK);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.STRONG);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.FEU, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.STRONG);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.WEAK);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.STRONG);
            this.put(Type.FEU, Weakness.STRONG);
            this.put(Type.GLACE, Weakness.STRONG);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.WEAK);
            this.put(Type.SOL, Weakness.WEAK);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.GLACE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.WEAK);
            this.put(Type.COMBAT, Weakness.WEAK);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.WEAK);
            this.put(Type.GLACE, Weakness.STRONG);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.WEAK);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.INSECTE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.STRONG);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.WEAK);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.WEAK);
            this.put(Type.SOL, Weakness.STRONG);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.WEAK);
        }});

        this.put(Type.NORMAL, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.WEAK);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.IGNORE);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.PLANTE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.STRONG);
            this.put(Type.ELECTRIQUE, Weakness.STRONG);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.WEAK);
            this.put(Type.GLACE, Weakness.WEAK);
            this.put(Type.INSECTE, Weakness.WEAK);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.WEAK);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.STRONG);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.WEAK);
        }});

        this.put(Type.POISON, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.STRONG);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.STRONG);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.STRONG);
            this.put(Type.PSY, Weakness.WEAK);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.WEAK);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.PSY, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.STRONG);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.WEAK);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.STRONG);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.WEAK);
            this.put(Type.TENEBRE, Weakness.WEAK);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.ROCHE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.WEAK);
            this.put(Type.COMBAT, Weakness.WEAK);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.WEAK);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.STRONG);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.STRONG);
            this.put(Type.PLANTE, Weakness.WEAK);
            this.put(Type.POISON, Weakness.STRONG);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.WEAK);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.STRONG);
        }});

        this.put(Type.SOL, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.NORMAL);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.WEAK);
            this.put(Type.ELECTRIQUE, Weakness.IGNORE);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.WEAK);
            this.put(Type.INSECTE, Weakness.NORMAL);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.WEAK);
            this.put(Type.POISON, Weakness.STRONG);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.STRONG);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.SPECTRE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.IGNORE);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.IGNORE);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.STRONG);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.WEAK);
            this.put(Type.TENEBRE, Weakness.WEAK);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.TENEBRE, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.WEAK);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.NORMAL);
            this.put(Type.FEE, Weakness.WEAK);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.NORMAL);
            this.put(Type.INSECTE, Weakness.WEAK);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.NORMAL);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.IGNORE);
            this.put(Type.ROCHE, Weakness.NORMAL);
            this.put(Type.SOL, Weakness.NORMAL);
            this.put(Type.SPECTRE, Weakness.STRONG);
            this.put(Type.TENEBRE, Weakness.STRONG);
            this.put(Type.VOL, Weakness.NORMAL);
        }});

        this.put(Type.VOL, new HashMap<Type, Weakness>(){{
            this.put(Type.ACIER, Weakness.NORMAL);
            this.put(Type.COMBAT, Weakness.STRONG);
            this.put(Type.DRAGON, Weakness.NORMAL);
            this.put(Type.EAU, Weakness.NORMAL);
            this.put(Type.ELECTRIQUE, Weakness.WEAK);
            this.put(Type.FEE, Weakness.NORMAL);
            this.put(Type.FEU, Weakness.NORMAL);
            this.put(Type.GLACE, Weakness.WEAK);
            this.put(Type.INSECTE, Weakness.STRONG);
            this.put(Type.NORMAL, Weakness.NORMAL);
            this.put(Type.PLANTE, Weakness.STRONG);
            this.put(Type.POISON, Weakness.NORMAL);
            this.put(Type.PSY, Weakness.NORMAL);
            this.put(Type.ROCHE, Weakness.WEAK);
            this.put(Type.SOL, Weakness.IGNORE);
            this.put(Type.SPECTRE, Weakness.NORMAL);
            this.put(Type.TENEBRE, Weakness.NORMAL);
            this.put(Type.VOL, Weakness.NORMAL);
        }});        
    }};
}
