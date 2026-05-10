import base_types
import Action17
import AuthorisationResult19

class CardPaymentTransaction145(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_AuthstnRslt"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=Action17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult19, min=1, max=1, mutex_group=None, array=False),
	))

