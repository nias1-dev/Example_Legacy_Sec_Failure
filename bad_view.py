def signup_poor(request):
    """Endpoint represents a security risk even though it properly sanitizes the fields. Improvement represented in
    security_signup() where view is not accessible by unauthorized accounts. View for demo purposes, not connected to model."""

    if request.method == "POST":
        form = SignupPoor(request.POST)
        if form.is_valid():
            return render(request, 'success.html')
    else:
        form = SignupPoor()

    return render(request, 'sign_up_poor_form.html', {'form': form})
