import numpy as np
import PhenomD

# from nonstd_gwaves.waveforms import kappa_waveform
import matplotlib.pyplot as plt


def test_phase_phenomD():
    theta = np.array([20.0, 19.99, -0.95, -0.95])
    Mf0 = 0.003
    Mf1 = 0.11
    f_l = Mf0 / ((theta[0] + theta[1]) * 4.92549094830932e-6)
    f_u = Mf1 / ((theta[0] + theta[1]) * 4.92549094830932e-6)
    del_f = 0.001
    f = np.arange(f_l, f_u, del_f)
    Mf = f * (theta[0] + theta[1]) * 4.92549094830932e-6

    phase, f1, f2, f_RD, f_damp = PhenomD.Phase(f, theta)

    plt.figure(figsize=(7, 5))
    plt.plot(Mf, phase, label="PhenomD")
    plt.axvline(x=f1 * (theta[0] + theta[1]) * 4.92549094830932e-6)
    plt.axvline(x=f2 * (theta[0] + theta[1]) * 4.92549094830932e-6)
    plt.axvline(
        x=f_RD * (theta[0] + theta[1]) * 4.92549094830932e-6, ls="--", color="C1"
    )
    plt.legend()
    plt.xlabel(r"Mf")
    plt.ylabel(r"$\Phi$")
    # plt.xlim(0.004, 0.018)
    # plt.ylim(-50, 200)
    plt.savefig("test_phase_full.pdf", bbox_inches="tight")

    phase_deriv = np.gradient(phase, del_f)
    print("derivative", -phase_deriv)
    plt.figure(figsize=(6, 5))
    plt.loglog(Mf, -phase_deriv, label="PhenomD")
    plt.axvline(x=f1 * (theta[0] + theta[1]) * 4.92549094830932e-6)
    plt.axvline(x=f2 * (theta[0] + theta[1]) * 4.92549094830932e-6)
    plt.axvline(
        x=f_RD * (theta[0] + theta[1]) * 4.92549094830932e-6, ls="--", color="C1"
    )
    plt.legend()
    plt.xlabel(r"Mf")
    plt.ylabel(r"$\Phi^{\prime}$")
    plt.xlim(Mf0, Mf1)
    plt.savefig("test_phase_derivative_full.pdf", bbox_inches="tight")

    # coeffs = PhenomD.get_coeffs(theta)
    # print(coeffs)
    return None


def test_Amp_phenomD():
    theta = np.array([20.0, 19.99, -0.95, -0.95])
    Mf0 = 0.003
    Mf1 = 0.11
    f_l = Mf0 / ((theta[0] + theta[1]) * 4.92549094830932e-6)
    f_u = Mf1 / ((theta[0] + theta[1]) * 4.92549094830932e-6)
    del_f = 0.001
    f = np.arange(f_l, f_u, del_f)
    Mf = f * (theta[0] + theta[1]) * 4.92549094830932e-6

    Amp, f3, f4 = PhenomD.Amp(f, theta)

    plt.figure(figsize=(7, 5))
    plt.loglog(Mf, Amp, label="PhenomD")
    plt.axvline(
        x=((f3 + f4) / 2) * (theta[0] + theta[1]) * 4.92549094830932e-6,
        ls="--",
        color="C0",
    )
    plt.axvline(x=f3 * (theta[0] + theta[1]) * 4.92549094830932e-6, ls="--", color="C0")
    plt.axvline(x=f4 * (theta[0] + theta[1]) * 4.92549094830932e-6, ls="--", color="C0")
    plt.legend()
    plt.xlabel(r"Mf")
    plt.ylabel(r"Amplitude")
    plt.savefig("test_Amp_full.pdf", bbox_inches="tight")

    return None


def test_frequency_calc():
    theta = np.array([5.0, 4.0, 0.0, 0.0])
    m1, m2, chi1, chi2 = theta

    fRD, fdamp = PhenomD.get_fRD_fdamp(m1, m2, chi1, chi2)
    print(fRD, fdamp)
    return None


if __name__ == "__main__":
    test_Amp_phenomD()
    # test_phase_phenomD()
    # test_frequency_calc()
