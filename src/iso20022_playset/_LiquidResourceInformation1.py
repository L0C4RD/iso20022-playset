# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AmountAndDirection102
from . import Max35Text
from . import TrueFalseIndicator

class LiquidResourceInformation1(base_types._BaseFieldType):

	__slots__ = ["_AgcyArrgmnts", "_AsstNcmbrd", "_CntrPtyId", "_LqdRsrcVal", "_MktVal", "_QlfygRsrc", "_Scrd"]
	@property
	def AgcyArrgmnts(self):
		return self._AgcyArrgmnts

	@AgcyArrgmnts.setter
	def AgcyArrgmnts(self, value):
		self._AgcyArrgmnts = value if value is not None else base_types.UninitialisedField(self, 'AgcyArrgmnts', TrueFalseIndicator, False)

	@AgcyArrgmnts.deleter
	def AgcyArrgmnts(self):
		del self._AgcyArrgmnts
		self._AgcyArrgmnts = base_types.UninitialisedField(self, 'AgcyArrgmnts', TrueFalseIndicator, False)

	@property
	def AsstNcmbrd(self):
		return self._AsstNcmbrd

	@AsstNcmbrd.setter
	def AsstNcmbrd(self, value):
		self._AsstNcmbrd = value if value is not None else base_types.UninitialisedField(self, 'AsstNcmbrd', TrueFalseIndicator, False)

	@AsstNcmbrd.deleter
	def AsstNcmbrd(self):
		del self._AsstNcmbrd
		self._AsstNcmbrd = base_types.UninitialisedField(self, 'AsstNcmbrd', TrueFalseIndicator, False)

	@property
	def CntrPtyId(self):
		return self._CntrPtyId

	@CntrPtyId.setter
	def CntrPtyId(self, value):
		self._CntrPtyId = value if value is not None else base_types.UninitialisedField(self, 'CntrPtyId', Max35Text, False)

	@CntrPtyId.deleter
	def CntrPtyId(self):
		del self._CntrPtyId
		self._CntrPtyId = base_types.UninitialisedField(self, 'CntrPtyId', Max35Text, False)

	@property
	def LqdRsrcVal(self):
		return self._LqdRsrcVal

	@LqdRsrcVal.setter
	def LqdRsrcVal(self, value):
		self._LqdRsrcVal = value if value is not None else base_types.UninitialisedField(self, 'LqdRsrcVal', AmountAndDirection102, False)

	@LqdRsrcVal.deleter
	def LqdRsrcVal(self):
		del self._LqdRsrcVal
		self._LqdRsrcVal = base_types.UninitialisedField(self, 'LqdRsrcVal', AmountAndDirection102, False)

	@property
	def MktVal(self):
		return self._MktVal

	@MktVal.setter
	def MktVal(self, value):
		self._MktVal = value if value is not None else base_types.UninitialisedField(self, 'MktVal', AmountAndDirection102, False)

	@MktVal.deleter
	def MktVal(self):
		del self._MktVal
		self._MktVal = base_types.UninitialisedField(self, 'MktVal', AmountAndDirection102, False)

	@property
	def QlfygRsrc(self):
		return self._QlfygRsrc

	@QlfygRsrc.setter
	def QlfygRsrc(self, value):
		self._QlfygRsrc = value if value is not None else base_types.UninitialisedField(self, 'QlfygRsrc', TrueFalseIndicator, False)

	@QlfygRsrc.deleter
	def QlfygRsrc(self):
		del self._QlfygRsrc
		self._QlfygRsrc = base_types.UninitialisedField(self, 'QlfygRsrc', TrueFalseIndicator, False)

	@property
	def Scrd(self):
		return self._Scrd

	@Scrd.setter
	def Scrd(self, value):
		self._Scrd = value if value is not None else base_types.UninitialisedField(self, 'Scrd', TrueFalseIndicator, False)

	@Scrd.deleter
	def Scrd(self):
		del self._Scrd
		self._Scrd = base_types.UninitialisedField(self, 'Scrd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgcyArrgmnts', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AsstNcmbrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrPtyId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LqdRsrcVal', type=AmountAndDirection102, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktVal', type=AmountAndDirection102, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QlfygRsrc', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Scrd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
	))