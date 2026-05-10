import base_types
import Max35Text

class OrganisationIdentification5(base_types._BaseFieldType):

	__slots__ = ["_RegrNm", "_RegnNb"]
	@property
	def RegrNm(self):
		return self._RegrNm

	@RegrNm.setter
	def RegrNm(self, value):
		self._RegrNm = value if type(value) != auto else self.make_default("RegrNm")

	@RegrNm.deleter
	def RegrNm(self):
		del self._RegrNm
		self._RegrNm = None

	@property
	def RegnNb(self):
		return self._RegnNb

	@RegnNb.setter
	def RegnNb(self, value):
		self._RegnNb = value if type(value) != auto else self.make_default("RegnNb")

	@RegnNb.deleter
	def RegnNb(self):
		del self._RegnNb
		self._RegnNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RegrNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnNb', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

