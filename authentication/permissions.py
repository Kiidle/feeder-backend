from django.contrib.auth.models import Group, Permission


def create_verify_permission_and_group():
    # create verify_user permission
    permission, created = Permission.objects.get_or_create(
        codename="verify_user",
        name="Can verify user",
        content_type__app_label="auth",
    )

    # create verified group, if not exists
    group, created = Group.objects.get_or_create(name="verified")

    # add the permission to the verified group
    group.permissions.add(permission)


def create_assignmod_permission_and_group():
    # create assign_moderator permission
    permission, created = Permission.objects.get_or_create(
        codename="assign_moderator",
        name="Can assign moderator",
        content_type__app_label="auth",
    )

    # create moderator group, if not exists
    group, created = Group.objects.get_or_create(name="moderator")

    # add the permission to the moderator group
    group.permissions.add(permission)
