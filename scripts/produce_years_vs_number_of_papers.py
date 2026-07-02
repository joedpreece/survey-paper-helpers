#%%
from matplotlib import pyplot as plt

from survey_paper_helpers.utils import load_data

df = load_data()

#%%
s_year = df.groupby("Year").size()

s_year_cum = s_year.cumsum()

width_mm = 89
height_mm = 89
width_inches = width_mm / 25.4
height_inches = width_inches * (2/3)

plt.rcParams.update({'font.size': 5})

fig, ax = plt.subplots(
    figsize=(width_inches, height_inches),
    dpi=300,
)

s_year.plot(ax=ax)
s_year_cum.plot(ax=ax)

ax.legend(["Yearly Studies", "Cumulative Studies"])

ax.set_title("Studies per Year")
ax.set_xlabel("Year")
ax.set_ylabel("Number of Studies")
fig.tight_layout()

# plt.show()
plt.savefig("./../artifacts/Figure_Studies_per_year.pdf")