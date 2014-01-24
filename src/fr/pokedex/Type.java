package fr.pokedex;


public enum Type {
    NONE (""),
    ACIER ("Acier"),
    COMBAT ("Combat"),
    DRAGON ("Combat"),
    EAU ("Combat"),
    ELECTRIQUE ("Combat"),
    FEE ("Combat"),
    FEU ("Combat"),
    GLACE ("Combat"),
    INSECTE ("Combat"),
    NORMAL ("Combat"),
    PLANTE ("Combat"),
    POISON ("Combat"),
    PSY ("Combat"),
    ROCHE ("Combat"),
    SOL ("Combat"),
    SPECTRE ("Combat"),
    TENEBRE ("Combat"),
    VOL ("Combat");
    
    public String display;
    private Type(String display) {
        this.display = display;
    }
}
