from . import base_types
from .BaselineStatus3Code import BaselineStatus3Code
from .ISODateTime import ISODateTime
from .Max140Text import Max140Text

class TransactionStatus5(base_types._BaseFieldType):

	__slots__ = ["_ChngDtTm", "_Sts", "_Desc"]
	@property
	def ChngDtTm(self):
		return self._ChngDtTm

	@ChngDtTm.setter
	def ChngDtTm(self, value):
		self._ChngDtTm = value if type(value) != base_types.auto else self.make_default("ChngDtTm")

	@ChngDtTm.deleter
	def ChngDtTm(self):
		del self._ChngDtTm
		self._ChngDtTm = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if type(value) != base_types.auto else self.make_default("Desc")

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChngDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BaselineStatus3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
	))

