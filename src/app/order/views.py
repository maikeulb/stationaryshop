
@lenses.route('/checkout', methods=['GET', 'POST'])
def checkout(order):

    cart_items = Cart.
            .all()
    focal_lengths = FocalLength.query \
            .all()
    form = LensForm()
    form.mount_id.choices = [(f.id, f.name) for f in mounts]
    form.focal_length_id.choices = [(f.id, f.name) for f in focal_lengths]
    if form.validate_on_submit():
        lens = Lens()
        form.populate_obj(lens)
        try:
            db.session.add(lens)
            db.session.commit()
            flash('Lens added!', 'success')
            return redirect(url_for('lenses.index'))
        except:
            db.session.rollback()
            flash('Error editing lens.', 'danger')

