import base_types
import YesNoIndicator
import ISODateTime
import CopyDuplicate1Code
import BusinessMessagePriorityCode
import Max35Text
import UnicodeChartsCode
import Party44Choice
import SignatureEnvelope

class BusinessApplicationHeader5(base_types._BaseFieldType):

	__slots__ = ["_Sgntr", "_CreDt", "_To", "_BizMsgIdr", "_Fr", "_CpyDplct", "_MsgDefIdr", "_PssblDplct", "_BizSvc", "_Prty", "_CharSet"]
	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if type(value) != auto else self.make_default("Sgntr")

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = None

	@property
	def CreDt(self):
		return self._CreDt

	@CreDt.setter
	def CreDt(self, value):
		self._CreDt = value if type(value) != auto else self.make_default("CreDt")

	@CreDt.deleter
	def CreDt(self):
		del self._CreDt
		self._CreDt = None

	@property
	def To(self):
		return self._To

	@To.setter
	def To(self, value):
		self._To = value if type(value) != auto else self.make_default("To")

	@To.deleter
	def To(self):
		del self._To
		self._To = None

	@property
	def BizMsgIdr(self):
		return self._BizMsgIdr

	@BizMsgIdr.setter
	def BizMsgIdr(self, value):
		self._BizMsgIdr = value if type(value) != auto else self.make_default("BizMsgIdr")

	@BizMsgIdr.deleter
	def BizMsgIdr(self):
		del self._BizMsgIdr
		self._BizMsgIdr = None

	@property
	def Fr(self):
		return self._Fr

	@Fr.setter
	def Fr(self, value):
		self._Fr = value if type(value) != auto else self.make_default("Fr")

	@Fr.deleter
	def Fr(self):
		del self._Fr
		self._Fr = None

	@property
	def CpyDplct(self):
		return self._CpyDplct

	@CpyDplct.setter
	def CpyDplct(self, value):
		self._CpyDplct = value if type(value) != auto else self.make_default("CpyDplct")

	@CpyDplct.deleter
	def CpyDplct(self):
		del self._CpyDplct
		self._CpyDplct = None

	@property
	def MsgDefIdr(self):
		return self._MsgDefIdr

	@MsgDefIdr.setter
	def MsgDefIdr(self, value):
		self._MsgDefIdr = value if type(value) != auto else self.make_default("MsgDefIdr")

	@MsgDefIdr.deleter
	def MsgDefIdr(self):
		del self._MsgDefIdr
		self._MsgDefIdr = None

	@property
	def PssblDplct(self):
		return self._PssblDplct

	@PssblDplct.setter
	def PssblDplct(self, value):
		self._PssblDplct = value if type(value) != auto else self.make_default("PssblDplct")

	@PssblDplct.deleter
	def PssblDplct(self):
		del self._PssblDplct
		self._PssblDplct = None

	@property
	def BizSvc(self):
		return self._BizSvc

	@BizSvc.setter
	def BizSvc(self, value):
		self._BizSvc = value if type(value) != auto else self.make_default("BizSvc")

	@BizSvc.deleter
	def BizSvc(self):
		del self._BizSvc
		self._BizSvc = None

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if type(value) != auto else self.make_default("Prty")

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = None

	@property
	def CharSet(self):
		return self._CharSet

	@CharSet.setter
	def CharSet(self, value):
		self._CharSet = value if type(value) != auto else self.make_default("CharSet")

	@CharSet.deleter
	def CharSet(self):
		del self._CharSet
		self._CharSet = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sgntr', type=SignatureEnvelope, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='To', type=Party44Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizMsgIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Fr', type=Party44Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CpyDplct', type=CopyDuplicate1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgDefIdr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PssblDplct', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BizSvc', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=BusinessMessagePriorityCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CharSet', type=UnicodeChartsCode, min=0, max=1, mutex_group=None, array=False),
	))

