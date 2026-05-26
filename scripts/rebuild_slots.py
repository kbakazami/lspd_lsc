"""
Script de reconstruction des slots 02-07 de academie.astro
à partir du contenu du PDF Police Academy.
"""

import os

path = r'E:\Projets\lspd_lsc\src\pages\academie.astro'

NEW_SLOTS = """\
          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">
            <div class="space-y-10">

              <!-- I. Codes Ten -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">I.</span>
                  <h4 class="font-display text-base font-semibold text-text">Codes Ten</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <img src="/academie/pa_codes_ten.jpg" alt="Codes Ten" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
              </div>

              <!-- II. Codes Purs -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">II.</span>
                  <h4 class="font-display text-base font-semibold text-text">Codes purs</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-2 gap-3 text-sm">
                  <div class="flex gap-3 px-4 py-3 border border-border bg-bg" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-lspd-navy shrink-0 pt-0.5 tracking-wider">Code 1</span><span class="text-text-muted text-xs leading-relaxed">Patrouille / intervention sans gyrophare ni sirène.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-lspd-navy shrink-0 pt-0.5 tracking-wider">Code 2</span><span class="text-text-muted text-xs leading-relaxed">Prise d'appel d'urgence — gyrophares activés mais sans sirène.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-danger/25 bg-danger/5" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-danger shrink-0 pt-0.5 tracking-wider">Code 3</span><span class="text-text-muted text-xs leading-relaxed">Appel prioritaire (situation critique uniquement) — gyro + sirène activés.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-border bg-bg" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-lspd-navy shrink-0 pt-0.5 tracking-wider">Code 4</span><span class="text-text-muted text-xs leading-relaxed">Fin de l'intervention — aucune assistance nécessaire.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-border bg-bg" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-lspd-navy shrink-0 pt-0.5 tracking-wider">Code 5</span><span class="text-text-muted text-xs leading-relaxed">En surveillance — les autres unités doivent éviter la zone.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-border bg-bg" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-lspd-navy shrink-0 pt-0.5 tracking-wider">Code 6</span><span class="text-text-muted text-xs leading-relaxed">En intervention.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-warning shrink-0 pt-0.5 tracking-wider">Code 99</span><span class="text-text-muted text-xs leading-relaxed">Enfilez votre gilet par balles.</span></div>
                  <div class="flex gap-3 px-4 py-3 border border-danger/40 bg-danger/10" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] font-bold text-danger shrink-0 pt-0.5 tracking-wider">Code Rouge</span><span class="text-text-muted text-xs leading-relaxed">Officier en danger — toutes unités s'y rendent, autorisation État-Major.</span></div>
                </div>
              </div>

              <!-- III. Indicatifs radio -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">III.</span>
                  <h4 class="font-display text-base font-semibold text-text">Indicatifs radio</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <img src="/academie/pa_indicatifs.jpg" alt="Indicatifs radio" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
              </div>

              <!-- IV. Alphabet phonetique -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">IV.</span>
                  <h4 class="font-display text-base font-semibold text-text">Alphabet phonétique de l'OTAN</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <p class="text-sm text-text-muted leading-relaxed mb-4">Sert à transmettre des messages susceptibles d'être mal compris — par exemple la communication d'une plaque d'immatriculation, pour éviter toute répétition en cas d'incompréhension.</p>
                <img src="/academie/pa_alphabet.jpg" alt="Alphabet phonetique OTAN" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
              </div>

              <!-- V. Regles de la radio -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">V.</span>
                  <h4 class="font-display text-base font-semibold text-text">Règles de la radio</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4 text-sm text-text-muted">
                  <div class="flex items-center gap-4 px-5 py-3 bg-lspd-navy-deep" style="border-radius: var(--radius-sm)">
                    <span class="font-mono text-[10px] tracking-[0.25em] uppercase text-lspd-gold/70 shrink-0">3 mots clés</span>
                    <span class="font-display text-lg font-semibold text-white">Court · Clair · Concis</span>
                  </div>
                  <ul class="space-y-2 leading-relaxed">
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Ne jamais couper une transmission.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Être concis et efficace — transmettre le plus rapidement possible.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Parler clairement — bien articuler, bien enclencher sa radio avant de parler pour éviter les répétitions.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Ne pas raconter sa vie — privilégiez le téléphone (TPH) pour les communications non opérationnelles.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Prioriser l'information — les infos utiles uniquement.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Rester professionnel — le vouvoiement est de rigueur.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Toujours prévenir d'un off-radio (10-6) et de son retour en service.</span></li>
                  </ul>
                  <div class="px-4 py-3 bg-bg border border-border font-mono text-xs" style="border-radius: var(--radius-sm)">
                    <span class="text-lspd-gold/70 uppercase tracking-widest text-[10px]">Format d'appel radio</span><br />
                    <span class="text-text">De "vous" à "l'appelé"</span> <span class="text-text-muted">ou</span> <span class="text-text">"l'appelé" pour "vous"</span>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- ── SLOT 3 — Les procedures ───────────────────────────── -->
        <div class="accordion-item border border-border bg-surface overflow-hidden" style="border-radius: var(--radius-md)">
          <button class="accordion-btn w-full flex items-center justify-between gap-6 px-6 py-5 text-left hover:bg-bg transition-colors" aria-expanded="false">
            <div class="flex items-center gap-5">
              <span class="shrink-0 text-[11px] font-mono text-lspd-gold/50 tabular-nums">03</span>
              <h3 class="font-display text-lg font-semibold text-text">Les procédures</h3>
            </div>
            <svg class="accordion-chevron shrink-0 text-text-subtle transition-transform duration-200" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">
            <div class="space-y-10">

              <!-- I. Interpellation individu -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">I.</span>
                  <h4 class="font-display text-base font-semibold text-text">Interpellation d'un individu</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4">
                  <img src="/academie/pa_interpellation.jpg" alt="Interpellation individu" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
                  <ol class="space-y-2 text-sm text-text-muted">
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">01</span><span>Menotter l'individu.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">02</span><span>Palper l'individu et saisir les armes si présentes.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">03</span><span>Sécuriser l'individu dans le véhicule de service.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">04</span><span>Amener l'individu au poste.</span></li>
                  </ol>
                </div>
              </div>

              <!-- II. Procedure au poste -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">II.</span>
                  <h4 class="font-display text-base font-semibold text-text">Procédure au poste</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4">
                  <img src="/academie/pa_procedure_poste.jpg" alt="Procedure au poste" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
                  <ol class="space-y-2 text-sm text-text-muted">
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">05</span><span>Prendre l'identité de l'individu.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">06</span><span>Lire les droits Miranda.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">07</span><span>Fouiller l'individu.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">08</span><span>Saisir tout objet illégal.</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">09</span><span>Faire déposer tous les effets personnels dans un bac (téléphone, ceinture, bijoux, lacets…)</span></li>
                    <li class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0 pt-0.5">10</span><span>Mettre l'individu en cellule.</span></li>
                  </ol>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- ── SLOT 4 — Les armes ────────────────────────────────── -->
        <div class="accordion-item border border-border bg-surface overflow-hidden" style="border-radius: var(--radius-md)">
          <button class="accordion-btn w-full flex items-center justify-between gap-6 px-6 py-5 text-left hover:bg-bg transition-colors" aria-expanded="false">
            <div class="flex items-center gap-5">
              <span class="shrink-0 text-[11px] font-mono text-lspd-gold/50 tabular-nums">04</span>
              <h3 class="font-display text-lg font-semibold text-text">Les armes</h3>
            </div>
            <svg class="accordion-chevron shrink-0 text-text-subtle transition-transform duration-200" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">
            <div class="space-y-4 text-sm text-text-muted">
              <div class="px-4 py-3 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                <div class="flex items-center gap-2 mb-2"><span class="font-mono text-[11px] font-bold text-lspd-navy">D1</span><span class="text-[10px] font-mono tracking-widest uppercase text-text-subtle">— Infraction</span></div>
                <p class="text-xs text-text-muted mb-2">Armes blanches, contondantes et armes par destination</p>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Matraque</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Poing américain</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Couteau de chasse</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Hachette</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Dague</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Cran d'arrêt</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Queue de billard</span>
                </div>
              </div>
              <div class="px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                <div class="flex items-center gap-2 mb-2"><span class="font-mono text-[11px] font-bold text-warning">B2</span><span class="text-[10px] font-mono tracking-widest uppercase text-text-subtle">— Délit mineur</span></div>
                <p class="text-xs text-text-muted mb-2">Armes de poing</p>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Glock</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Beretta</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Calibre 50+</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Pétoire</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Revolver cal.44</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Pistolet lourd</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Pistolet vintage</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Pistolet de détresse</span>
                </div>
              </div>
              <div class="px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                <div class="flex items-center gap-2 mb-2"><span class="font-mono text-[11px] font-bold text-warning">A2</span><span class="text-[10px] font-mono tracking-widest uppercase text-text-subtle">— Délit mineur</span></div>
                <p class="text-xs text-text-muted mb-2">Armes incapacitantes</p>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Taser</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Fumigène</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Grenade lacrymogène</span>
                </div>
              </div>
              <div class="px-4 py-3 border border-danger/25 bg-danger/5" style="border-radius: var(--radius-sm)">
                <div class="flex items-center gap-2 mb-2"><span class="font-mono text-[11px] font-bold text-danger">C</span><span class="text-[10px] font-mono tracking-widest uppercase text-text-subtle">— Délit majeur</span></div>
                <p class="text-xs text-text-muted mb-2">Armes de chasse</p>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Mousquet</span>
                </div>
              </div>
              <div class="px-4 py-3 border border-danger/25 bg-danger/5" style="border-radius: var(--radius-sm)">
                <div class="flex items-center gap-2 mb-2"><span class="font-mono text-[11px] font-bold text-danger">B1</span><span class="text-[10px] font-mono tracking-widest uppercase text-text-subtle">— Délit majeur</span></div>
                <p class="text-xs text-text-muted mb-2">Armes automatiques et semi-automatiques</p>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Mac-10</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Uzi</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Tec-9</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Skorpion</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Remington</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Mossberg 500</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Mossberg 590A1</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Canon scié</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">AA-12</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Saiga 12</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">UTS-15</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">MP5</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">AKU</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Thompson</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">AK47</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">M4</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">G63c</span>
                </div>
              </div>
              <div class="px-4 py-3 border border-danger/40 bg-danger/10" style="border-radius: var(--radius-sm)">
                <div class="flex items-center gap-2 mb-2"><span class="font-mono text-[11px] font-bold text-danger">A1</span><span class="text-[10px] font-mono tracking-widest uppercase text-text-subtle">— Crime</span></div>
                <p class="text-xs text-text-muted mb-2">Armes de guerre et explosifs</p>
                <div class="flex flex-wrap gap-1.5">
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Lance-roquettes</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Lance-grenades</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Mines</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">C4</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Grenade</span>
                  <span class="px-2 py-0.5 text-[11px] bg-surface border border-border" style="border-radius: var(--radius-sm)">Cocktail Molotov</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- ── SLOT 5 — Divisions & Grades ──────────────────────── -->
        <div class="accordion-item border border-border bg-surface overflow-hidden" style="border-radius: var(--radius-md)">
          <button class="accordion-btn w-full flex items-center justify-between gap-6 px-6 py-5 text-left hover:bg-bg transition-colors" aria-expanded="false">
            <div class="flex items-center gap-5">
              <span class="shrink-0 text-[11px] font-mono text-lspd-gold/50 tabular-nums">05</span>
              <h3 class="font-display text-lg font-semibold text-text">Divisions & Grades</h3>
            </div>
            <svg class="accordion-chevron shrink-0 text-text-subtle transition-transform duration-200" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">
            <div class="space-y-10">

              <!-- I. Les divisions -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">I.</span>
                  <h4 class="font-display text-base font-semibold text-text">Les divisions</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-2 gap-3">
                  <div class="flex gap-4 items-start p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_swat.jpg" alt="SWAT" class="w-10 h-10 object-contain shrink-0" />
                    <div><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-0.5">SWAT</p><p class="text-[11px] font-semibold text-text mb-1">Special Weapons And Tactics</p><p class="text-xs text-text-muted leading-relaxed">Unité d'intervention chargée des opérations armées sur des lieux à risques.</p></div>
                  </div>
                  <div class="flex gap-4 items-start p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_cid.jpg" alt="CID" class="w-10 h-10 object-contain shrink-0" />
                    <div><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-0.5">CID</p><p class="text-[11px] font-semibold text-text mb-1">Criminal Investigation Division</p><p class="text-xs text-text-muted leading-relaxed">Division d'enquêtes liées aux groupuscules criminels et leurs activités.</p></div>
                  </div>
                  <div class="flex gap-4 items-start p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_td.jpg" alt="TD" class="w-10 h-10 object-contain shrink-0" />
                    <div><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-0.5">TD</p><p class="text-[11px] font-semibold text-text mb-1">Traffic Division</p><p class="text-xs text-text-muted leading-relaxed">Division chargée de la gestion de crises, des relations médias et de la promotion du poste.</p></div>
                  </div>
                  <div class="flex gap-4 items-start p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_k9.jpg" alt="K-9" class="w-10 h-10 object-contain shrink-0" />
                    <div><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-0.5">K-9 Unit</p><p class="text-[11px] font-semibold text-text mb-1">Canine Division</p><p class="text-xs text-text-muted leading-relaxed">Division canine, centralisée sur le dépistage des drogues et des explosifs.</p></div>
                  </div>
                  <div class="flex gap-4 items-start p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_asd.jpg" alt="ASD" class="w-10 h-10 object-contain shrink-0" />
                    <div><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-0.5">ASD</p><p class="text-[11px] font-semibold text-text mb-1">Air Support Division</p><p class="text-xs text-text-muted leading-relaxed">Division chargée des appareils aériens, du circuit aérien et de sa réglementation.</p></div>
                  </div>
                  <div class="flex gap-4 items-start p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_pa.jpg" alt="PA" class="w-10 h-10 object-contain shrink-0" />
                    <div><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-0.5">PA</p><p class="text-[11px] font-semibold text-text mb-1">Police Academy</p><p class="text-xs text-text-muted leading-relaxed">Division chargée des recrutements, formations, entraînements et de l'accompagnement des cadets et officiers.</p></div>
                  </div>
                </div>
              </div>

              <!-- II. La hierarchie -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">II.</span>
                  <h4 class="font-display text-base font-semibold text-text">La hiérarchie (ordre décroissant)</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-1.5 text-sm">
                  <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold shrink-0 pt-0.5 tabular-nums w-5">13</span><span class="font-semibold text-white">Chief</span><span class="text-white/50 text-xs ml-2">L'officier de police le plus haut gradé.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy/10 border border-lspd-navy/15" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold shrink-0 pt-0.5 tabular-nums w-5">12</span><span class="font-semibold text-text">Commandant</span><span class="text-text-muted text-xs ml-2">Dirige plusieurs postes de police. Assiste le Chief.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy/10 border border-lspd-navy/15" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold shrink-0 pt-0.5 tabular-nums w-5">11</span><span class="font-semibold text-text">Capitaine</span><span class="text-text-muted text-xs ml-2">Dirige un poste de police.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy/10 border border-lspd-navy/15" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold shrink-0 pt-0.5 tabular-nums w-5">10</span><span class="font-semibold text-text">Lieutenant</span><span class="text-text-muted text-xs ml-2">Direction des bureaux. Commande les agents en l'absence du Capitaine.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">09</span><span class="font-semibold text-text">Sergent-Chef / Watch Commander</span><span class="text-text-muted text-xs ml-2">Commande les sergents.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">08</span><span class="font-semibold text-text">Sergent</span><span class="text-text-muted text-xs ml-2">Commande les officiers. Peut appartenir à n'importe quel bureau.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">07</span><span class="font-semibold text-text">Officier III</span><span class="text-text-muted text-xs ml-2">Peut devenir FTI.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">06</span><span class="font-semibold text-text">Senior Lead Officier (SLO)</span><span class="text-text-muted text-xs ml-2">Expérience terrain renforcée. Dirige les officiers en l'absence de haut gradé.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">05</span><span class="font-semibold text-text">Officier II</span><span class="text-text-muted text-xs ml-2">Peut gérer le rôle de Dispatcher. Peut devenir FTO.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">04</span><span class="font-semibold text-text">Officier I</span><span class="text-text-muted text-xs ml-2">Connaît ses calls radio. Peut rejoindre un Bureau ou une Spécialité.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">03</span><span class="font-semibold text-text">Officier</span><span class="text-text-muted text-xs ml-2">A terminé sa formation académique. Complète sa formation sur le terrain avec son instructeur.</span></div>
                  <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[10px] text-lspd-gold/60 shrink-0 pt-0.5 tabular-nums w-5">01</span><span class="font-semibold text-text">Academy (Cadet)</span><span class="text-text-muted text-xs ml-2">Formation initiale avant d'accéder au grade d'Officier.</span></div>
                </div>
              </div>

              <!-- III. Les corps -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">III.</span>
                  <h4 class="font-display text-base font-semibold text-text">Les corps</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-2 gap-3 text-sm">
                  <div class="p-4 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-1">Command Staff (CS)</p><p class="text-white/70 text-xs leading-relaxed">Le corps exécutif prend les décisions majeures du LSPD, vote les changements importants et peut superviser les opérations sur le terrain.</p></div>
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)"><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-1">Supervisor (SUP)</p><p class="text-text-muted text-xs leading-relaxed">Encadre le personnel, gère promotions et sanctions, et veille au bon déroulement des opérations ainsi qu'à la discipline radio.</p></div>
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)"><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-1">FTI / FTO</p><p class="text-text-muted text-xs leading-relaxed">Le corps de formation accompagne les nouvelles recrues, assure leur apprentissage sur le terrain et leur transmet les procédures du département.</p></div>
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)"><p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-1">Officier</p><p class="text-text-muted text-xs leading-relaxed">Corps principal chargé des patrouilles, interventions et procédures quotidiennes pour assurer la sécurité de la ville.</p></div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- ── SLOT 6 — Equipements & Vehicules ──────────────────── -->
        <div class="accordion-item border border-border bg-surface overflow-hidden" style="border-radius: var(--radius-md)">
          <button class="accordion-btn w-full flex items-center justify-between gap-6 px-6 py-5 text-left hover:bg-bg transition-colors" aria-expanded="false">
            <div class="flex items-center gap-5">
              <span class="shrink-0 text-[11px] font-mono text-lspd-gold/50 tabular-nums">06</span>
              <h3 class="font-display text-lg font-semibold text-text">Équipements & Véhicules</h3>
            </div>
            <svg class="accordion-chevron shrink-0 text-text-subtle transition-transform duration-200" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">
            <div class="space-y-10">

              <!-- I. Tenue reglementaire -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">I.</span>
                  <h4 class="font-display text-base font-semibold text-text">Tenue réglementaire</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4">
                  <div class="overflow-hidden" style="border-radius: var(--radius-sm)">
                    <img src="/academie/image_tenue.png" alt="Schéma annoté de la tenue LSPD" class="w-full object-contain" />
                  </div>
                  <div class="flex items-start gap-3 px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" class="shrink-0 mt-0.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                    <p class="text-sm text-text-muted leading-relaxed">Le port du <strong class="text-text font-medium">holster et du badge est obligatoire</strong>. Les manches longues sont obligatoires pour les officiers de base.</p>
                  </div>
                </div>
              </div>

              <!-- II. Equipement de base -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">II.</span>
                  <h4 class="font-display text-base font-semibold text-text">Équipement de base</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-2 gap-3 text-xs text-text-muted">
                  <div class="flex gap-3 p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_glock.jpg" alt="Glock 17" class="w-14 h-14 object-contain shrink-0" />
                    <div><p class="font-semibold text-text text-sm mb-1">Glock 17</p><p>Pistolet semi-automatique</p><p>Munition : 9×19 mm Parabellum</p><p>Capacité : 12 coups</p></div>
                  </div>
                  <div class="flex gap-3 p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_taser.jpg" alt="Taser" class="w-14 h-14 object-contain shrink-0" />
                    <div><p class="font-semibold text-text text-sm mb-1">Taser X26</p><p>Pistolet à impulsion électrique</p><p>Puissance : 2 milliampères</p><p>Capacité : 1 coup</p></div>
                  </div>
                  <div class="flex gap-3 p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_matraque.jpg" alt="Matraque" class="w-14 h-14 object-contain shrink-0" />
                    <div><p class="font-semibold text-text text-sm mb-1">Matraque</p><p>Arme de contact moins létale</p><p>Portée : corps à corps</p></div>
                  </div>
                  <div class="flex gap-3 p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <div class="w-14 h-14 flex items-center justify-center shrink-0 text-text-subtle">
                      <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
                    </div>
                    <div><p class="font-semibold text-text text-sm mb-1">Lampe torche tactique</p><p>Type : LED rechargeable</p><p>Puissance : 800 à 2 000 lumens</p><p>Batterie : lithium-ion 3 000–5 000 mAh</p></div>
                  </div>
                </div>
              </div>

              <!-- III. Armement avance -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">III.</span>
                  <h4 class="font-display text-base font-semibold text-text">Armement avancé</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-3 gap-3 text-xs text-text-muted">
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_m4.jpg" alt="M4" class="w-full h-20 object-contain mb-3" />
                    <p class="font-semibold text-text text-sm mb-1">Carabine M4</p>
                    <p>Automatique</p><p>Calibre 5.56×45 mm OTAN</p><p>Capacité : 30 cartouches</p>
                  </div>
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_shotgun.jpg" alt="Fusil à pompe" class="w-full h-20 object-contain mb-3" />
                    <p class="font-semibold text-text text-sm mb-1">Fusil à pompe</p>
                    <p>Rechargement à pompe</p><p>Calibre 12</p><p>Capacité : 6 coups</p>
                  </div>
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_mp5.jpg" alt="MP5" class="w-full h-20 object-contain mb-3" />
                    <p class="font-semibold text-text text-sm mb-1">MP5</p>
                    <p>Automatique / semi-auto</p><p>Calibre 9×19 mm Parabellum</p><p>Capacité : 15 à 30 cartouches</p>
                  </div>
                </div>
              </div>

              <!-- IV. Equipement specialise -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">IV.</span>
                  <h4 class="font-display text-base font-semibold text-text">Équipement spécialisé</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-2 gap-3 text-xs text-text-muted">
                  <div class="flex gap-3 p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_masque.jpg" alt="Masque tactique" class="w-14 h-14 object-contain shrink-0" />
                    <div><p class="font-semibold text-text text-sm mb-1">Masque tactique (Avon)</p><p>Protection CBRN / anti-émeute</p><p>Filtre : cartouches NATO 40 mm</p><p>Poids : 500 à 900 g</p></div>
                  </div>
                  <div class="flex gap-3 p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <img src="/academie/pa_gilet.jpg" alt="Gilet pare-balles" class="w-14 h-14 object-contain shrink-0" />
                    <div><p class="font-semibold text-text text-sm mb-1">Gilet pare-balles</p><p>Souple : 2–4 kg (Kevlar/Dyneema)</p><p>Avec plaques : 6–12 kg</p><p>Système MOLLE pour équipements</p></div>
                  </div>
                </div>
              </div>

              <!-- V. Vehicule de service -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">V.</span>
                  <h4 class="font-display text-base font-semibold text-text">Véhicule de service</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4">
                  <div class="grid sm:grid-cols-2 gap-3">
                    <img src="/academie/pa_voiture.jpg" alt="Véhicule de patrouille" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
                    <img src="/academie/pa_voiture2.jpg" alt="Véhicule de patrouille 2" class="w-full object-contain" style="border-radius: var(--radius-sm)" />
                  </div>
                  <div class="px-4 py-3 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <p class="text-[10px] font-mono tracking-[0.25em] uppercase text-lspd-gold mb-3">Composition de votre véhicule</p>
                    <ul class="grid sm:grid-cols-2 gap-2 text-sm text-text-muted">
                      <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-lspd-gold/50 shrink-0" style="border-radius:1px"></span>Ordinateur de bord (Panel)</li>
                      <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-lspd-gold/50 shrink-0" style="border-radius:1px"></span>Radio</li>
                      <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-lspd-gold/50 shrink-0" style="border-radius:1px"></span>Radar</li>
                      <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-lspd-gold/50 shrink-0" style="border-radius:1px"></span>Éthylomètre</li>
                      <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-lspd-gold/50 shrink-0" style="border-radius:1px"></span>Kit de premier secours</li>
                      <li class="flex items-center gap-2"><span class="w-1.5 h-1.5 bg-lspd-gold/50 shrink-0" style="border-radius:1px"></span>Signalisation routière (plots, barrières…)</li>
                    </ul>
                  </div>
                </div>
              </div>

              <!-- VI. Course-poursuite -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">VI.</span>
                  <h4 class="font-display text-base font-semibold text-text">Course-poursuite</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-3 text-sm text-text-muted leading-relaxed">
                  <ul class="space-y-2">
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Garder un minimum de distance avec le véhicule suivi pour éviter de lui rentrer dedans en cas de ralentissement soudain.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Respecter au maximum le code de la route — éviter la conduite sur les trottoirs ou en contre-sens quand c'est possible.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Off Road : adapter sa vitesse, les routes peuvent être dangereuses (nid de poule, rochers, bosses…)</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>C'est le copilote du véhicule de Lead qui fait les appels radio.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Le véhicule Secondaire anticipe les déplacements du véhicule suivi dans les ruelles et passages étroits.</span></li>
                    <li class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Le véhicule Secondaire est prêt à reprendre le Lead en cas d'accident du Leader.</span></li>
                  </ul>
                  <div class="flex items-start gap-3 px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                    <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" class="shrink-0 mt-0.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                    <p>En dehors des poursuites, respectez le code de la route. N'activez vos codes que lors d'une intervention ou d'une recherche de secteur.</p>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>

        <!-- ── SLOT 7 — ISTC & Regles de service ─────────────────── -->
        <div class="accordion-item border border-border bg-surface overflow-hidden" style="border-radius: var(--radius-md)">
          <button class="accordion-btn w-full flex items-center justify-between gap-6 px-6 py-5 text-left hover:bg-bg transition-colors" aria-expanded="false">
            <div class="flex items-center gap-5">
              <span class="shrink-0 text-[11px] font-mono text-lspd-gold/50 tabular-nums">07</span>
              <h3 class="font-display text-lg font-semibold text-text">ISTC & Règles de service</h3>
            </div>
            <svg class="accordion-chevron shrink-0 text-text-subtle transition-transform duration-200" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
              <polyline points="6 9 12 15 18 9"/>
            </svg>
          </button>
          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">
            <div class="space-y-10">

              <!-- I. ISTC CEVITAL -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">I.</span>
                  <h4 class="font-display text-base font-semibold text-text">ISTC / CEVITAL</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4 text-sm text-text-muted">
                  <p class="leading-relaxed">L'ISTC (Instruction au Tir de Combat) repose sur 4 règles fondamentales et une chronologie de tir en 7 temps : <strong class="text-text font-medium">CEVITAL</strong>.</p>
                  <div class="space-y-2">
                    <p class="text-[10px] font-mono tracking-[0.25em] uppercase text-lspd-gold">4 règles fondamentales</p>
                    <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0">01</span><span>Toute arme doit être considérée comme chargée.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0">02</span><span>Ne jamais pointer ou laisser pointer le canon sur quelque chose que l'on ne veut pas détruire.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0">03</span><span>Garder l'index hors de la détente tant que les organes de visée ne sont pas alignés sur l'objectif.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-bg border border-border" style="border-radius: var(--radius-sm)"><span class="font-mono text-[11px] text-lspd-gold font-bold shrink-0">04</span><span>Être sûr de son objectif et de son environnement.</span></div>
                  </div>
                  <div class="space-y-2">
                    <p class="text-[10px] font-mono tracking-[0.25em] uppercase text-lspd-gold">CEVITAL — Chronologie de tir en 7 temps</p>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">C</span><span class="text-white/80">Certitude de son objectif et de son environnement.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">E</span><span class="text-white/80">Élévation de l'arme à 45 degrés.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">V</span><span class="text-white/80">Visée : alignement des organes de visée sur l'objectif.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">I</span><span class="text-white/80">Index : placement de l'index sur la queue de détente.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">T</span><span class="text-white/80">Tir : pression continue sur la queue de détente jusqu'au tir.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">A</span><span class="text-white/80">Analyse de la cible — reprendre le tir si la cible n'est pas traitée.</span></div>
                    <div class="flex gap-3 px-4 py-2.5 bg-lspd-navy-deep border border-lspd-gold/20" style="border-radius: var(--radius-sm)"><span class="font-mono text-[13px] font-bold text-lspd-gold shrink-0 w-4">L</span><span class="text-white/80">Latéral : analyse latérale en recherche de danger / Liaison : avertir les médecins.</span></div>
                  </div>
                </div>
              </div>

              <!-- II. Tatouages & bijoux -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">II.</span>
                  <h4 class="font-display text-base font-semibold text-text">Tatouages & bijoux</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-2 text-sm text-text-muted leading-relaxed">
                  <div class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Les tatouages sont autorisés sous conditions : pas de tatouage au visage, et aucun tatouage entachant l'image du service.</span></div>
                  <div class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Cheveux longs : ils doivent être attachés de sorte à ne pas cacher la plaque de police.</span></div>
                  <div class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Le maquillage est autorisé, à condition qu'il ne soit pas excessif.</span></div>
                  <div class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-danger/60" style="border-radius:1px"></span><span>Les bijoux sont <strong class="text-text font-medium">interdits</strong> pendant le service. Seule exception : la montre.</span></div>
                </div>
              </div>

              <!-- III. Le respect -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">III.</span>
                  <h4 class="font-display text-base font-semibold text-text">Le respect hiérarchique</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="space-y-4 text-sm text-text-muted leading-relaxed">
                  <p>Lors de la <strong class="text-text font-medium">première rencontre</strong> avec un supérieur pendant les heures de service, s'adresser à lui ainsi :</p>
                  <div class="px-4 py-3 bg-bg border border-border font-mono text-xs space-y-1" style="border-radius: var(--radius-sm)">
                    <p class="text-lspd-gold/70 uppercase tracking-widest text-[10px] mb-2">Formules de salut</p>
                    <p class="text-text">&#x25B8; "Mes respects <em>Nom</em> !" — Officier I, II et III</p>
                    <p class="text-text">&#x25B8; "Mes respects Sergent !"</p>
                    <p class="text-text">&#x25B8; "Mes respects Sergent-Chef !"</p>
                    <p class="text-text">&#x25B8; "Mes respects mon Lieutenant !"</p>
                    <p class="text-text">&#x25B8; "Mes respects mon Capitaine !"</p>
                    <p class="text-text">&#x25B8; "Mes respects mon Commandant !"</p>
                    <p class="text-text">&#x25B8; "Mes respects Chief !"</p>
                  </div>
                  <div class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Au premier dispatch de la soirée : salut général et "mes respects" à votre arrivée en salle de dispatch.</span></div>
                  <div class="flex items-start gap-2.5"><span class="shrink-0 mt-1.5 w-1.5 h-1.5 bg-lspd-gold/50" style="border-radius:1px"></span><span>Après le premier salut, parlez normalement mais en gardant le respect. <strong class="text-text font-medium">Ce ne sont pas vos amis.</strong></span></div>
                  <div class="flex items-start gap-3 px-4 py-3 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#b45309" stroke-width="1.5" stroke-linecap="round" class="shrink-0 mt-0.5"><path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>
                    <span>Le <strong class="text-text font-medium">vouvoiement est obligatoire</strong> avec tous les collègues en permanence, en face à face comme par radio.</span>
                  </div>
                </div>
              </div>

              <!-- IV. Niveaux d'alertes -->
              <div>
                <div class="flex items-center gap-3 mb-4">
                  <span class="text-[10px] font-mono tracking-[0.3em] uppercase text-lspd-gold opacity-75">IV.</span>
                  <h4 class="font-display text-base font-semibold text-text">Niveaux d'alertes — DEFCON</h4>
                  <div class="flex-1 h-px bg-border"></div>
                </div>
                <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-3 text-xs text-text-muted">
                  <div class="p-4 bg-bg border border-border" style="border-radius: var(--radius-sm)">
                    <p class="font-mono text-[10px] tracking-widest uppercase text-lspd-gold mb-1">DEFCON 5</p>
                    <p class="font-semibold text-text text-sm mb-2">Situation normale</p>
                    <p class="mb-1">Équipement standard</p>
                    <p class="text-[10px] text-text-subtle">Niveau d'alerte le plus bas</p>
                  </div>
                  <div class="p-4 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                    <p class="font-mono text-[10px] tracking-widest uppercase text-warning mb-1">DEFCON 4</p>
                    <p class="font-semibold text-text text-sm mb-2">Vigilance renforcée</p>
                    <p class="mb-0.5">Durée max 48h / renouv. 78h</p>
                    <p class="mb-0.5">Droits : palpation sous conditions</p>
                    <p>Arme longue disponible</p>
                  </div>
                  <div class="p-4 border border-warning/25 bg-warning/5" style="border-radius: var(--radius-sm)">
                    <p class="font-mono text-[10px] tracking-widest uppercase text-warning mb-1">DEFCON 3</p>
                    <p class="font-semibold text-text text-sm mb-2">Menace élevée</p>
                    <p class="mb-0.5">Durée max 48h / renouv. 48h</p>
                    <p class="mb-0.5">Droits : palpation + contrôle</p>
                    <p>Arme longue autorisée</p>
                  </div>
                  <div class="p-4 border border-danger/25 bg-danger/5" style="border-radius: var(--radius-sm)">
                    <p class="font-mono text-[10px] tracking-widest uppercase text-danger mb-1">DEFCON 2</p>
                    <p class="font-semibold text-text text-sm mb-2">Crise majeure</p>
                    <p class="mb-0.5">Durée max 48h / renouv. 24h</p>
                    <p class="mb-0.5">Droits : palpation + barrages + contrôle</p>
                    <p>Équipement tactique — NOOSE partiel</p>
                  </div>
                  <div class="p-4 border border-danger/40 bg-danger/10" style="border-radius: var(--radius-sm)">
                    <p class="font-mono text-[10px] tracking-widest uppercase text-danger mb-1">DEFCON 1</p>
                    <p class="font-semibold text-text text-sm mb-2">État d'urgence</p>
                    <p class="mb-0.5">Durée max 48h / renouv. 24h</p>
                    <p class="mb-0.5">Droits : palpation + contrôle + couvre-feu</p>
                    <p>Armement maximal — NOOSE complet</p>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>"""

with open(path, encoding='utf-8') as f:
    content = f.read()

start_marker = '          <div class="accordion-panel hidden border-t border-border px-6 pb-8 pt-6">\n            <div class="space-y-10">\n\n              <!-- I. Autorité -->'
end_marker = '        </div>        </div>'

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)
end_idx_full = end_idx + len(end_marker)

if start_idx == -1 or end_idx == -1:
    print("ERROR: markers not found")
    print(f"start_marker found: {start_idx != -1}")
    print(f"end_marker found: {end_idx != -1}")
else:
    new_content = content[:start_idx] + NEW_SLOTS + '\n' + content[end_idx_full:]
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Done. File written. Size: {len(new_content)} chars")
    print(f"Replaced {end_idx_full - start_idx} chars with {len(NEW_SLOTS)} chars")
