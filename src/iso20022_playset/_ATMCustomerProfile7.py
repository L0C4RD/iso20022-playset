from . import base_types
from ._ATMService28 import ATMService28
from ._Max35Text import Max35Text
from ._Max70Text import Max70Text

class ATMCustomerProfile7(base_types._BaseFieldType):

	__slots__ = ["_AllwdSvcs", "_CstmrId", "_PrflDesc", "_PrflRef"]
	@property
	def AllwdSvcs(self):
		return self._AllwdSvcs

	@AllwdSvcs.setter
	def AllwdSvcs(self, value):
		self._AllwdSvcs = value if type(value) != base_types.auto else self.make_default("AllwdSvcs")

	@AllwdSvcs.deleter
	def AllwdSvcs(self):
		del self._AllwdSvcs
		self._AllwdSvcs = None

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if type(value) != base_types.auto else self.make_default("CstmrId")

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = None

	@property
	def PrflDesc(self):
		return self._PrflDesc

	@PrflDesc.setter
	def PrflDesc(self, value):
		self._PrflDesc = value if type(value) != base_types.auto else self.make_default("PrflDesc")

	@PrflDesc.deleter
	def PrflDesc(self):
		del self._PrflDesc
		self._PrflDesc = None

	@property
	def PrflRef(self):
		return self._PrflRef

	@PrflRef.setter
	def PrflRef(self, value):
		self._PrflRef = value if type(value) != base_types.auto else self.make_default("PrflRef")

	@PrflRef.deleter
	def PrflRef(self):
		del self._PrflRef
		self._PrflRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AllwdSvcs', type=ATMService28, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CstmrId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflDesc', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrflRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

