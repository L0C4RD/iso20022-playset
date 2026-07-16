# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ChequeDeliveryMethod1Choice
from . import ChequeType2Code
from . import ISODate
from . import Max35Text
from . import Max70Text
from . import NameAndAddress18
from . import Priority2Code

class Cheque19(base_types._BaseFieldType):

	__slots__ = ["_ChqFr", "_ChqMtrtyDt", "_ChqNb", "_ChqTp", "_DlvrTo", "_DlvryMtd", "_FrmsCd", "_InstrPrty", "_MemoFld", "_PrtLctn", "_RgnlClrZone", "_Sgntr"]
	@property
	def ChqFr(self):
		return self._ChqFr

	@ChqFr.setter
	def ChqFr(self, value):
		self._ChqFr = value if value is not None else base_types.UninitialisedField(self, 'ChqFr', NameAndAddress18, False)

	@ChqFr.deleter
	def ChqFr(self):
		del self._ChqFr
		self._ChqFr = base_types.UninitialisedField(self, 'ChqFr', NameAndAddress18, False)

	@property
	def ChqMtrtyDt(self):
		return self._ChqMtrtyDt

	@ChqMtrtyDt.setter
	def ChqMtrtyDt(self, value):
		self._ChqMtrtyDt = value if value is not None else base_types.UninitialisedField(self, 'ChqMtrtyDt', ISODate, False)

	@ChqMtrtyDt.deleter
	def ChqMtrtyDt(self):
		del self._ChqMtrtyDt
		self._ChqMtrtyDt = base_types.UninitialisedField(self, 'ChqMtrtyDt', ISODate, False)

	@property
	def ChqNb(self):
		return self._ChqNb

	@ChqNb.setter
	def ChqNb(self, value):
		self._ChqNb = value if value is not None else base_types.UninitialisedField(self, 'ChqNb', Max35Text, False)

	@ChqNb.deleter
	def ChqNb(self):
		del self._ChqNb
		self._ChqNb = base_types.UninitialisedField(self, 'ChqNb', Max35Text, False)

	@property
	def ChqTp(self):
		return self._ChqTp

	@ChqTp.setter
	def ChqTp(self, value):
		self._ChqTp = value if value is not None else base_types.UninitialisedField(self, 'ChqTp', ChequeType2Code, False)

	@ChqTp.deleter
	def ChqTp(self):
		del self._ChqTp
		self._ChqTp = base_types.UninitialisedField(self, 'ChqTp', ChequeType2Code, False)

	@property
	def DlvrTo(self):
		return self._DlvrTo

	@DlvrTo.setter
	def DlvrTo(self, value):
		self._DlvrTo = value if value is not None else base_types.UninitialisedField(self, 'DlvrTo', NameAndAddress18, False)

	@DlvrTo.deleter
	def DlvrTo(self):
		del self._DlvrTo
		self._DlvrTo = base_types.UninitialisedField(self, 'DlvrTo', NameAndAddress18, False)

	@property
	def DlvryMtd(self):
		return self._DlvryMtd

	@DlvryMtd.setter
	def DlvryMtd(self, value):
		self._DlvryMtd = value if value is not None else base_types.UninitialisedField(self, 'DlvryMtd', ChequeDeliveryMethod1Choice, False)

	@DlvryMtd.deleter
	def DlvryMtd(self):
		del self._DlvryMtd
		self._DlvryMtd = base_types.UninitialisedField(self, 'DlvryMtd', ChequeDeliveryMethod1Choice, False)

	@property
	def FrmsCd(self):
		return self._FrmsCd

	@FrmsCd.setter
	def FrmsCd(self, value):
		self._FrmsCd = value if value is not None else base_types.UninitialisedField(self, 'FrmsCd', Max35Text, False)

	@FrmsCd.deleter
	def FrmsCd(self):
		del self._FrmsCd
		self._FrmsCd = base_types.UninitialisedField(self, 'FrmsCd', Max35Text, False)

	@property
	def InstrPrty(self):
		return self._InstrPrty

	@InstrPrty.setter
	def InstrPrty(self, value):
		self._InstrPrty = value if value is not None else base_types.UninitialisedField(self, 'InstrPrty', Priority2Code, False)

	@InstrPrty.deleter
	def InstrPrty(self):
		del self._InstrPrty
		self._InstrPrty = base_types.UninitialisedField(self, 'InstrPrty', Priority2Code, False)

	@property
	def MemoFld(self):
		return self._MemoFld

	@MemoFld.setter
	def MemoFld(self, value):
		self._MemoFld = value if value is not None else base_types.UninitialisedField(self, 'MemoFld', Max35Text, True)

	@MemoFld.deleter
	def MemoFld(self):
		del self._MemoFld
		self._MemoFld = base_types.UninitialisedField(self, 'MemoFld', Max35Text, True)

	@property
	def PrtLctn(self):
		return self._PrtLctn

	@PrtLctn.setter
	def PrtLctn(self, value):
		self._PrtLctn = value if value is not None else base_types.UninitialisedField(self, 'PrtLctn', Max35Text, False)

	@PrtLctn.deleter
	def PrtLctn(self):
		del self._PrtLctn
		self._PrtLctn = base_types.UninitialisedField(self, 'PrtLctn', Max35Text, False)

	@property
	def RgnlClrZone(self):
		return self._RgnlClrZone

	@RgnlClrZone.setter
	def RgnlClrZone(self, value):
		self._RgnlClrZone = value if value is not None else base_types.UninitialisedField(self, 'RgnlClrZone', Max35Text, False)

	@RgnlClrZone.deleter
	def RgnlClrZone(self):
		del self._RgnlClrZone
		self._RgnlClrZone = base_types.UninitialisedField(self, 'RgnlClrZone', Max35Text, False)

	@property
	def Sgntr(self):
		return self._Sgntr

	@Sgntr.setter
	def Sgntr(self, value):
		self._Sgntr = value if value is not None else base_types.UninitialisedField(self, 'Sgntr', Max70Text, True)

	@Sgntr.deleter
	def Sgntr(self):
		del self._Sgntr
		self._Sgntr = base_types.UninitialisedField(self, 'Sgntr', Max70Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChqFr', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqMtrtyDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ChqTp', type=ChequeType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvrTo', type=NameAndAddress18, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryMtd', type=ChequeDeliveryMethod1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmsCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrty', type=Priority2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MemoFld', type=Max35Text, min=0, max=2, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtLctn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RgnlClrZone', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sgntr', type=Max70Text, min=0, max=5, mutex_group=None, array=True),
	))