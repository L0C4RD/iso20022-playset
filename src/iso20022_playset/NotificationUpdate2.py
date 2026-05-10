from . import base_types
from .Max35Text import Max35Text
from .YesNoIndicator import YesNoIndicator

class NotificationUpdate2(base_types._BaseFieldType):

	__slots__ = ["_RcnfrmInstrs", "_PrvsNtfctnId"]
	@property
	def RcnfrmInstrs(self):
		return self._RcnfrmInstrs

	@RcnfrmInstrs.setter
	def RcnfrmInstrs(self, value):
		self._RcnfrmInstrs = value if type(value) != auto else self.make_default("RcnfrmInstrs")

	@RcnfrmInstrs.deleter
	def RcnfrmInstrs(self):
		del self._RcnfrmInstrs
		self._RcnfrmInstrs = None

	@property
	def PrvsNtfctnId(self):
		return self._PrvsNtfctnId

	@PrvsNtfctnId.setter
	def PrvsNtfctnId(self, value):
		self._PrvsNtfctnId = value if type(value) != auto else self.make_default("PrvsNtfctnId")

	@PrvsNtfctnId.deleter
	def PrvsNtfctnId(self):
		del self._PrvsNtfctnId
		self._PrvsNtfctnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RcnfrmInstrs', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrvsNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

