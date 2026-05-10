from . import base_types
from .MarginCallResult2Choice import MarginCallResult2Choice
from .ActiveCurrencyAndAmount import ActiveCurrencyAndAmount

class MarginCallResult3(base_types._BaseFieldType):

	__slots__ = ["_DfltFndAmt", "_MrgnCallRslt"]
	@property
	def DfltFndAmt(self):
		return self._DfltFndAmt

	@DfltFndAmt.setter
	def DfltFndAmt(self, value):
		self._DfltFndAmt = value if type(value) != base_types.auto else self.make_default("DfltFndAmt")

	@DfltFndAmt.deleter
	def DfltFndAmt(self):
		del self._DfltFndAmt
		self._DfltFndAmt = None

	@property
	def MrgnCallRslt(self):
		return self._MrgnCallRslt

	@MrgnCallRslt.setter
	def MrgnCallRslt(self, value):
		self._MrgnCallRslt = value if type(value) != base_types.auto else self.make_default("MrgnCallRslt")

	@MrgnCallRslt.deleter
	def MrgnCallRslt(self):
		del self._MrgnCallRslt
		self._MrgnCallRslt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='DfltFndAmt', type=ActiveCurrencyAndAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MrgnCallRslt', type=MarginCallResult2Choice, min=1, max=1, mutex_group=None, array=False),
	))

