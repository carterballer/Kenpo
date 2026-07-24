st.set_page_config(page_title="Kenpo Practice Generator", page_icon="🥋")

st.title("🥋 Kenpo Practice Generator")

file_path = st.file_uploader("Upload your forms Excel file", type=["xlsx"])

if file_path is not None:

    # 1. Read all sheets into a dictionary ONCE (Fast)
    sheets_dict = pd.read_excel(file_path, sheet_name=None)
    form_names = list(sheets_dict.keys())

    # Extract all data categories cleanly
    punches, kicks, ranks, styles = [], [], [], []

    for name, df in sheets_dict.items():
        if "Punches" in df.columns:
            punches.extend(df["Punches"].dropna().tolist())
        if "Kicks" in df.columns:
            kicks.extend(df["Kicks"].dropna().tolist())
        if "Rank" in df.columns:
            ranks.extend(df["Rank"].dropna().tolist())
        if "Style" in df.columns:
            styles.extend(df["Style"].dropna().tolist())

    # Drop duplicates & sort lists
    punches = sorted(list(dict.fromkeys(punches)))
    kicks = sorted(list(dict.fromkeys(kicks)))
    ranks = sorted(list(dict.fromkeys(ranks)))
    styles = sorted(list(dict.fromkeys(styles)))

    st.success(f"Successfully loaded {len(form_names)} forms!")

    # 2. Add a Button to Regenerate Practice Routine
    if st.button("🔄 Generate New Routine", type="primary"):
        st.divider()

        practice_forms = []

        # --- PUNCH SECTION ---
        if punches:
            punch = random.choice(punches)
            if punch in [
                "Front Two Knuckle",
                "Back Two Knuckle",
                "Thrust",
                "Inverted Thrust",
                "Hook",
                "U",
            ]:
                st.subheader(f"🥊 Practice your **{punch}** Punch:")
            elif punch in ["Hon Tsuki", "Snake"]:
                st.subheader(f"🥊 Practice your **{punch}** Strike:")
            else:
                st.subheader(f"🥊 Practice your **{punch}**: ")

            matched_forms = []
            for name, df in sheets_dict.items():
                if "Punches" in df.columns and punch in df["Punches"].values:
                    matched_forms.append(name)
                    practice_forms.append(name)

            for f in matched_forms:
                st.write(f"• {f}")

        # --- KICK SECTION ---
        if kicks:
            kick = random.choice(kicks)
            if kick == "Rising Knee":
                st.subheader(f"🦵 Practice your **{kick}**:")
            else:
                st.subheader(f"🦵 Practice your **{kick}** Kick:")

            matched_forms = []
            for name, df in sheets_dict.items():
                if "Kicks" in df.columns and kick in df["Kicks"].values:
                    matched_forms.append(name)
                    practice_forms.append(name)

            for f in matched_forms:
                st.write(f"• {f}")

        # --- RANK SECTION ---
        if ranks:
            rank = random.choice(ranks)
            if rank in [
                "Beginner",
                "Intermediate",
                "Advanced",
                "Sankyu",
                "Nikkyu",
                "Ikkyu",
                "Shodan",
                "Nidan",
            ]:
                st.subheader(f"🥋 Practice your **{rank}** forms:")
            else:
                st.subheader(f"🥋 Practice your **{rank}** Belt forms:")

            matched_forms = []
            for name, df in sheets_dict.items():
                if "Rank" in df.columns and rank in df["Rank"].values:
                    matched_forms.append(name)
                    practice_forms.append(name)

            for f in matched_forms:
                st.write(f"• {f}")

        # --- STYLE SECTION ---
        if styles:
            style = random.choice(styles)
            if style == "Blocking":
                st.subheader(f"☯️ Practice your **{style}** Systems:")
            elif style in ["Fist Set", "Kata", "Pinian", "Ning Li"]:
                st.subheader(f"☯️ Practice your **{style}s**:")
            else:
                st.subheader(f"☯️ Practice your **{style}** forms:")

            matched_forms = []
            for name, df in sheets_dict.items():
                if "Style" in df.columns and style in df["Style"].values:
                    matched_forms.append(name)
                    practice_forms.append(name)

            for f in matched_forms:
                st.write(f"• {f}")

        # --- SUMMARY LIST ---
        st.divider()
        practice_forms = sorted(list(dict.fromkeys(practice_forms)))
        st.markdown(
            f"### 📋 Concise List of Forms ({len(practice_forms)} total)"
        )
        for form in practice_forms:
            st.write(f"✅ **{form}**")
