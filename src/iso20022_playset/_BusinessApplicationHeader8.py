# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BusinessMessagePriorityCode
from . import CopyDuplicate1Code
from . import ISODateTime
from . import ImplementationSpecification1
from . import Max35Text
from . import Party51Choice
from . import SignatureEnvelope
from . import UnicodeChartsCode
from . import YesNoIndicator

class BusinessApplicationHeader8(base_types._BaseFieldType):

	__slots__ = ["_BizMsgIdr", "_BizPrcgDt", "_BizSvc", "_CharSet", "_CpyDplct", "_CreDt", "_Fr", "_MktPrctc", "_MsgDefIdr", "_Prty", "_PssblDplct", "_Sgntr", "_To"]
	@property
	def BizMsgIdr(self):
		return self._BizMsgIdr

	@BizMsgIdr.setter
	def BizMsgIdr(self, value):
		self._BizMsgIdr = value if value is not None else base_types.UninitialisedField(self, 'BizMsgIdr', Max35Text, False)

	@BizMsgIdr.deleter
	def BizMsgIdr(self):
		del self._BizMsgIdr
		self._BizMsgIdr = base_types.UninitialisedField(self, 'BizMsgIdr', Max35Text, False)

	@property
	def BizPrcgDt(self):
		return self._BizPrcgDt

	@BizPrcgDt.setter
	def BizPrcgDt(self, value):
		self._BizPrcgDt = value if value is not None else base_types.UninitialisedField(self, 'BizPrcgDt', ISODateTime, False)

	@BizPrcgDt.deleter
	def BizPrcgDt(self):
		del self._BizPrcgDt
		self._BizPrcgDt = base_types.UninitialisedField(self, 'BizPrcgDt', ISODateTime, False)

	@property
	def BizSvc(self):
		return self._BizSvc

	@BizSvc.setter
	def BizSvc(self, value):
		self._BizSvc = value if value is not None else base_types.UninitialisedField(self, 'BizSvc', Max35Text, False)

	@BizSvc.deleter
	def BizSvc(self):
		del self._BizSvc
		self._BizSvc = base_types.UninitialisedField(self, 'BizSvc', Max35Text, False)

	@property
	def CharSet(self):
		return self._CharSet

	@CharSet.setter
	def CharSet(self, value):
		self._CharSet = value if value is not None else base_types.UninitialisedField(self, 'CharSet', UnicodeChartsCode, False)

	@CharSet.deleter
	def CharSet(self):
		del self._CharSet
		self._CharSet = base_types.UninitialisedField(self, 'CharSet', UnicodeChartsCode, False)

	@property
	def CpyDplct(self):
		return self._CpyDplct

	@CpyDplct.setter
	def CpyDplct(self, value):
		self._CpyDplct = value if value is not None else base_types.UninitialisedField(self, 'CpyDplct', CopyDuplicate1Code, False)

	@CpyDplct.deleter
	def CpyDplct(self):
		del self._CpyDplct
		self._CpyDplct = base_types.UninitialisedField(self, 'CpyDplct', CopyDuplicate1Code, False)

	@property
	def CreDt(self):
		return self._CreDt

	@CreDt.setter
	def CreDt(self, value):
		self._CreDt = value if value is not None else base_types.UninitialisedField(self, 'CreDt', ISODateTime, False)

	@CreDt.deleter
	def CreDt(self):
		del self._CreDt
		self._CreDt = base_types.UninitialisedField(self, 'CreDt', ISODateTime, False)

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if value is not None else base_types.UninitialisedField(self, 'Fr', Party51Choice, False)

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = base_types.UninitialisedField(self, 'Fr', Party51Choice, False)

	@property
	def MktPrctc(self):
		return self._MktPrctc

	@MktPrctc.setter
	def MktPrctc(self, value):
		self._MktPrctc = value if value is not None else base_types.UninitialisedField(self, 'MktPrctc', ImplementationSpecification1, False)

	@MktPrctc.deleter
	def MktPrctc(self):
		del self._MktPrctc
		self._MktPrctc = base_types.UninitialisedField(self, 'MktPrctc', ImplementationSpecification1, False)

	@property
	def MsgDefIdr(self):
		return self._MsgDefIdr

	@MsgDefIdr.setter
	def MsgDefIdr(self, value):
		self._MsgDefIdr = value if value is not None else base_types.UninitialisedField(self, 'MsgDefIdr', Max35Text, False)

	@MsgDefIdr.deleter
	def MsgDefIdr(self):
		del self._MsgDefIdr
		self._MsgDefIdr = base_types.UninitialisedField(self, 'MsgDefIdr', Max35Text, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', BusinessMessagePriorityCode, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', BusinessMessagePriorityCode, False)

	@property
	def PssblDplct(self):
		return self._PssblDplct

	@PssblDplct.setter
	def PssblDplct(self, value):
		self._PssblDplct = value if value is not None else base_types.UninitialisedField(self, 'PssblDplct', YesNoIndicator, False)

	@PssblDplct.deleter
	def PssblDplct(self):
		del self._PssblDplct
		self._PssblDplct = base_types.UninitialisedField(self, 'PssblDplct', YesNoIndicator, False)

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if value is not None else base_types.UninitialisedField(self, 'Sgntr', SignatureEnvelope, False)

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = base_types.UninitialisedField(self, 'Sgntr', SignatureEnvelope, False)

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if value is not None else base_types.UninitialisedField(self, 'To', Party51Choice, False)

	@To.deleter
	def To(self):
		del self._To
		self._To = base_types.UninitialisedField(self, 'To', Party51Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizMsgIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizPrcgDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizSvc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CharSet', type=UnicodeChartsCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDplct', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=Party51Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktPrctc', type=ImplementationSpecification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDefIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=BusinessMessagePriorityCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssblDplct', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=SignatureEnvelope, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=Party51Choice, min=1, max=1, mutex_group=None, array=False),
	))