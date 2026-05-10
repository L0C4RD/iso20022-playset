from . import base_types
import Action17
import AuthorisationResult17
import AmountAndDirection93
import ContentInformationType40
import CurrencyConversion29
import Product4
import Product5

class CardPaymentTransaction144(base_types._BaseFieldType):

	__slots__ = ["_Bal", "_AddtlAvlblPdct", "_Actn", "_PrtctdBal", "_CcyConvsElgblty", "_AuthstnRslt", "_AllwdPdctCd", "_NotAllwdPdctCd"]
	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def AddtlAvlblPdct(self):
		return self._AddtlAvlblPdct

	@AddtlAvlblPdct.setter
	def AddtlAvlblPdct(self, value):
		self._AddtlAvlblPdct = value if type(value) != auto else self.make_default("AddtlAvlblPdct")

	@AddtlAvlblPdct.deleter
	def AddtlAvlblPdct(self):
		del self._AddtlAvlblPdct
		self._AddtlAvlblPdct = None

	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def PrtctdBal(self):
		return self._PrtctdBal

	@PrtctdBal.setter
	def PrtctdBal(self, value):
		self._PrtctdBal = value if type(value) != auto else self.make_default("PrtctdBal")

	@PrtctdBal.deleter
	def PrtctdBal(self):
		del self._PrtctdBal
		self._PrtctdBal = None

	@property
	def CcyConvsElgblty(self):
		return self._CcyConvsElgblty

	@CcyConvsElgblty.setter
	def CcyConvsElgblty(self, value):
		self._CcyConvsElgblty = value if type(value) != auto else self.make_default("CcyConvsElgblty")

	@CcyConvsElgblty.deleter
	def CcyConvsElgblty(self):
		del self._CcyConvsElgblty
		self._CcyConvsElgblty = None

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if type(value) != auto else self.make_default("AuthstnRslt")

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = None

	@property
	def AllwdPdctCd(self):
		return self._AllwdPdctCd

	@AllwdPdctCd.setter
	def AllwdPdctCd(self, value):
		self._AllwdPdctCd = value if type(value) != auto else self.make_default("AllwdPdctCd")

	@AllwdPdctCd.deleter
	def AllwdPdctCd(self):
		del self._AllwdPdctCd
		self._AllwdPdctCd = None

	@property
	def NotAllwdPdctCd(self):
		return self._NotAllwdPdctCd

	@NotAllwdPdctCd.setter
	def NotAllwdPdctCd(self, value):
		self._NotAllwdPdctCd = value if type(value) != auto else self.make_default("NotAllwdPdctCd")

	@NotAllwdPdctCd.deleter
	def NotAllwdPdctCd(self):
		del self._NotAllwdPdctCd
		self._NotAllwdPdctCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Bal', type=AmountAndDirection93, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlAvlblPdct', type=Product5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Actn', type=Action17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdBal', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsElgblty', type=CurrencyConversion29, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AllwdPdctCd', type=Product4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NotAllwdPdctCd', type=Product4, min=0, max=None, mutex_group=None, array=True),
	))

