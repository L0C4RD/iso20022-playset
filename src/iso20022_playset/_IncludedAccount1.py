from . import base_types
from .Max35Text import Max35Text
from .YesNoIndicator import YesNoIndicator

class IncludedAccount1(base_types._BaseFieldType):

	__slots__ = ["_InclInd", "_SctiesAcctId"]
	@property
	def InclInd(self):
		return self._InclInd

	@InclInd.setter
	def InclInd(self, value):
		self._InclInd = value if type(value) != base_types.auto else self.make_default("InclInd")

	@InclInd.deleter
	def InclInd(self):
		del self._InclInd
		self._InclInd = None

	@property
	def SctiesAcctId(self):
		return self._SctiesAcctId

	@SctiesAcctId.setter
	def SctiesAcctId(self, value):
		self._SctiesAcctId = value if type(value) != base_types.auto else self.make_default("SctiesAcctId")

	@SctiesAcctId.deleter
	def SctiesAcctId(self):
		del self._SctiesAcctId
		self._SctiesAcctId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InclInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesAcctId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

