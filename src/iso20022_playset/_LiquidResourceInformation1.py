from . import base_types
from .Max35Text import Max35Text
from .AmountAndDirection102 import AmountAndDirection102
from .TrueFalseIndicator import TrueFalseIndicator

class LiquidResourceInformation1(base_types._BaseFieldType):

	__slots__ = ["_CntrPtyId", "_AgcyArrgmnts", "_MktVal", "_Scrd", "_LqdRsrcVal", "_AsstNcmbrd", "_QlfygRsrc"]
	@property
	def CntrPtyId(self):
		return self._CntrPtyId

	@CntrPtyId.setter
	def CntrPtyId(self, value):
		self._CntrPtyId = value if type(value) != base_types.auto else self.make_default("CntrPtyId")

	@CntrPtyId.deleter
	def CntrPtyId(self):
		del self._CntrPtyId
		self._CntrPtyId = None

	@property
	def AgcyArrgmnts(self):
		return self._AgcyArrgmnts

	@AgcyArrgmnts.setter
	def AgcyArrgmnts(self, value):
		self._AgcyArrgmnts = value if type(value) != base_types.auto else self.make_default("AgcyArrgmnts")

	@AgcyArrgmnts.deleter
	def AgcyArrgmnts(self):
		del self._AgcyArrgmnts
		self._AgcyArrgmnts = None

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if type(value) != base_types.auto else self.make_default("MktVal")

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = None

	@property
	def Scrd(self):
		return self._Scrd

	@Scrd.setter
	def Scrd(self, value):
		self._Scrd = value if type(value) != base_types.auto else self.make_default("Scrd")

	@Scrd.deleter
	def Scrd(self):
		del self._Scrd
		self._Scrd = None

	@property
	def LqdRsrcVal(self):
		return self._LqdRsrcVal

	@LqdRsrcVal.setter
	def LqdRsrcVal(self, value):
		self._LqdRsrcVal = value if type(value) != base_types.auto else self.make_default("LqdRsrcVal")

	@LqdRsrcVal.deleter
	def LqdRsrcVal(self):
		del self._LqdRsrcVal
		self._LqdRsrcVal = None

	@property
	def AsstNcmbrd(self):
		return self._AsstNcmbrd

	@AsstNcmbrd.setter
	def AsstNcmbrd(self, value):
		self._AsstNcmbrd = value if type(value) != base_types.auto else self.make_default("AsstNcmbrd")

	@AsstNcmbrd.deleter
	def AsstNcmbrd(self):
		del self._AsstNcmbrd
		self._AsstNcmbrd = None

	@property
	def QlfygRsrc(self):
		return self._QlfygRsrc

	@QlfygRsrc.setter
	def QlfygRsrc(self, value):
		self._QlfygRsrc = value if type(value) != base_types.auto else self.make_default("QlfygRsrc")

	@QlfygRsrc.deleter
	def QlfygRsrc(self):
		del self._QlfygRsrc
		self._QlfygRsrc = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CntrPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AgcyArrgmnts', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdRsrcVal', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstNcmbrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QlfygRsrc', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
	))

