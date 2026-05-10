import base_types
import Max70Text
import ChequeType2Code
import NameAndAddress18
import ChequeDeliveryMethod1Choice
import Max35Text
import ISODate
import Priority2Code

class Cheque19(base_types._BaseFieldType):

	__slots__ = ["_ChqTp", "_ChqFr", "_ChqNb", "_RgnlClrZone", "_DlvrTo", "_PrtLctn", "_DlvryMtd", "_FrmsCd", "_InstrPrty", "_MemoFld", "_ChqMtrtyDt", "_Sgntr"]
	@property
	def ChqTp(self):
		return self._ChqTp

	@ChqTp.setter
	def ChqTp(self, value):
		self._ChqTp = value if type(value) != auto else self.make_default("ChqTp")

	@ChqTp.deleter
	def ChqTp(self):
		del self._ChqTp
		self._ChqTp = None

	@property
	def ChqFr(self):
		return self._ChqFr

	@ChqFr.setter
	def ChqFr(self, value):
		self._ChqFr = value if type(value) != auto else self.make_default("ChqFr")

	@ChqFr.deleter
	def ChqFr(self):
		del self._ChqFr
		self._ChqFr = None

	@property
	def ChqNb(self):
		return self._ChqNb

	@ChqNb.setter
	def ChqNb(self, value):
		self._ChqNb = value if type(value) != auto else self.make_default("ChqNb")

	@ChqNb.deleter
	def ChqNb(self):
		del self._ChqNb
		self._ChqNb = None

	@property
	def RgnlClrZone(self):
		return self._RgnlClrZone

	@RgnlClrZone.setter
	def RgnlClrZone(self, value):
		self._RgnlClrZone = value if type(value) != auto else self.make_default("RgnlClrZone")

	@RgnlClrZone.deleter
	def RgnlClrZone(self):
		del self._RgnlClrZone
		self._RgnlClrZone = None

	@property
	def DlvrTo(self):
		return self._DlvrTo

	@DlvrTo.setter
	def DlvrTo(self, value):
		self._DlvrTo = value if type(value) != auto else self.make_default("DlvrTo")

	@DlvrTo.deleter
	def DlvrTo(self):
		del self._DlvrTo
		self._DlvrTo = None

	@property
	def PrtLctn(self):
		return self._PrtLctn

	@PrtLctn.setter
	def PrtLctn(self, value):
		self._PrtLctn = value if type(value) != auto else self.make_default("PrtLctn")

	@PrtLctn.deleter
	def PrtLctn(self):
		del self._PrtLctn
		self._PrtLctn = None

	@property
	def DlvryMtd(self):
		return self._DlvryMtd

	@DlvryMtd.setter
	def DlvryMtd(self, value):
		self._DlvryMtd = value if type(value) != auto else self.make_default("DlvryMtd")

	@DlvryMtd.deleter
	def DlvryMtd(self):
		del self._DlvryMtd
		self._DlvryMtd = None

	@property
	def FrmsCd(self):
		return self._FrmsCd

	@FrmsCd.setter
	def FrmsCd(self, value):
		self._FrmsCd = value if type(value) != auto else self.make_default("FrmsCd")

	@FrmsCd.deleter
	def FrmsCd(self):
		del self._FrmsCd
		self._FrmsCd = None

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if type(value) != auto else self.make_default("InstrPrty")

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = None

	@property
	def MemoFld(self):
		return self._MemoFld

	@MemoFld.setter
	def MemoFld(self, value):
		self._MemoFld = value if type(value) != auto else self.make_default("MemoFld")

	@MemoFld.deleter
	def MemoFld(self):
		del self._MemoFld
		self._MemoFld = None

	@property
	def ChqMtrtyDt(self):
		return self._ChqMtrtyDt

	@ChqMtrtyDt.setter
	def ChqMtrtyDt(self, value):
		self._ChqMtrtyDt = value if type(value) != auto else self.make_default("ChqMtrtyDt")

	@ChqMtrtyDt.deleter
	def ChqMtrtyDt(self):
		del self._ChqMtrtyDt
		self._ChqMtrtyDt = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChqTp', type=ChequeType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqFr', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnlClrZone', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrTo', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryMtd', type=ChequeDeliveryMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmsCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MemoFld', type=Max35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='ChqMtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=Max70Text, min=0, max=5, mutex_group=None, array=True),
	))

