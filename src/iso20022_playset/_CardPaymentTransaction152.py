# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Action18
from . import AmountAndDirection93
from . import AuthorisationResult17
from . import ContentInformationType40
from . import CurrencyConversion34
from . import Product4
from . import Product5

class CardPaymentTransaction152(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_AddtlAvlblPdct", "_AllwdPdctCd", "_AuthstnRslt", "_Bal", "_CcyConvsElgblty", "_NotAllwdPdctCd", "_PrtctdBal"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if value is not None else base_types.UninitialisedField(self, 'Actn', Action18, True)

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = base_types.UninitialisedField(self, 'Actn', Action18, True)

	@property
	def AddtlAvlblPdct(self):
		return self._AddtlAvlblPdct

	@AddtlAvlblPdct.setter
	def AddtlAvlblPdct(self, value):
		self._AddtlAvlblPdct = value if value is not None else base_types.UninitialisedField(self, 'AddtlAvlblPdct', Product5, True)

	@AddtlAvlblPdct.deleter
	def AddtlAvlblPdct(self):
		del self._AddtlAvlblPdct
		self._AddtlAvlblPdct = base_types.UninitialisedField(self, 'AddtlAvlblPdct', Product5, True)

	@property
	def AllwdPdctCd(self):
		return self._AllwdPdctCd

	@AllwdPdctCd.setter
	def AllwdPdctCd(self, value):
		self._AllwdPdctCd = value if value is not None else base_types.UninitialisedField(self, 'AllwdPdctCd', Product4, True)

	@AllwdPdctCd.deleter
	def AllwdPdctCd(self):
		del self._AllwdPdctCd
		self._AllwdPdctCd = base_types.UninitialisedField(self, 'AllwdPdctCd', Product4, True)

	@property
	def AuthstnRslt(self):
		return self._AuthstnRslt

	@AuthstnRslt.setter
	def AuthstnRslt(self, value):
		self._AuthstnRslt = value if value is not None else base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult17, False)

	@AuthstnRslt.deleter
	def AuthstnRslt(self):
		del self._AuthstnRslt
		self._AuthstnRslt = base_types.UninitialisedField(self, 'AuthstnRslt', AuthorisationResult17, False)

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if value is not None else base_types.UninitialisedField(self, 'Bal', AmountAndDirection93, False)

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = base_types.UninitialisedField(self, 'Bal', AmountAndDirection93, False)

	@property
	def CcyConvsElgblty(self):
		return self._CcyConvsElgblty

	@CcyConvsElgblty.setter
	def CcyConvsElgblty(self, value):
		self._CcyConvsElgblty = value if value is not None else base_types.UninitialisedField(self, 'CcyConvsElgblty', CurrencyConversion34, False)

	@CcyConvsElgblty.deleter
	def CcyConvsElgblty(self):
		del self._CcyConvsElgblty
		self._CcyConvsElgblty = base_types.UninitialisedField(self, 'CcyConvsElgblty', CurrencyConversion34, False)

	@property
	def NotAllwdPdctCd(self):
		return self._NotAllwdPdctCd

	@NotAllwdPdctCd.setter
	def NotAllwdPdctCd(self, value):
		self._NotAllwdPdctCd = value if value is not None else base_types.UninitialisedField(self, 'NotAllwdPdctCd', Product4, True)

	@NotAllwdPdctCd.deleter
	def NotAllwdPdctCd(self):
		del self._NotAllwdPdctCd
		self._NotAllwdPdctCd = base_types.UninitialisedField(self, 'NotAllwdPdctCd', Product4, True)

	@property
	def PrtctdBal(self):
		return self._PrtctdBal

	@PrtctdBal.setter
	def PrtctdBal(self, value):
		self._PrtctdBal = value if value is not None else base_types.UninitialisedField(self, 'PrtctdBal', ContentInformationType40, False)

	@PrtctdBal.deleter
	def PrtctdBal(self):
		del self._PrtctdBal
		self._PrtctdBal = base_types.UninitialisedField(self, 'PrtctdBal', ContentInformationType40, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=Action18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AddtlAvlblPdct', type=Product5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AllwdPdctCd', type=Product4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AuthstnRslt', type=AuthorisationResult17, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=AmountAndDirection93, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CcyConvsElgblty', type=CurrencyConversion34, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NotAllwdPdctCd', type=Product4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtctdBal', type=ContentInformationType40, min=0, max=1, mutex_group=None, array=False),
	))