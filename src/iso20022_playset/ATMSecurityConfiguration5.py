import base_types
import PINFormat4Code
import Number

class ATMSecurityConfiguration5(base_types._BaseFieldType):

	__slots__ = ["_PINFrmt", "_PINLngthCpblties"]
	@property
	def PINFrmt(self):
		return self._PINFrmt

	@PINFrmt.setter
	def PINFrmt(self, value):
		self._PINFrmt = value if type(value) != auto else self.make_default("PINFrmt")

	@PINFrmt.deleter
	def PINFrmt(self):
		del self._PINFrmt
		self._PINFrmt = None

	@property
	def PINLngthCpblties(self):
		return self._PINLngthCpblties

	@PINLngthCpblties.setter
	def PINLngthCpblties(self, value):
		self._PINLngthCpblties = value if type(value) != auto else self.make_default("PINLngthCpblties")

	@PINLngthCpblties.deleter
	def PINLngthCpblties(self):
		del self._PINLngthCpblties
		self._PINLngthCpblties = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PINFrmt', type=PINFormat4Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PINLngthCpblties', type=Number, min=0, max=1, mutex_group=None, array=False),
	))

