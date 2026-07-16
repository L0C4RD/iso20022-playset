# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max35Text
from . import TaxAmount3
from . import TaxPeriod3

class TaxRecord3(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_CertId", "_Ctgy", "_CtgyDtls", "_DbtrSts", "_FrmsCd", "_Prd", "_TaxAmt", "_Tp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', Max140Text, False)

	@property
	def CertId(self):
		return self._CertId

	@CertId.setter
	def CertId(self, value):
		self._CertId = value if value is not None else base_types.UninitialisedField(self, 'CertId', Max35Text, False)

	@CertId.deleter
	def CertId(self):
		del self._CertId
		self._CertId = base_types.UninitialisedField(self, 'CertId', Max35Text, False)

	@property
	def Ctgy(self):
		return self._Ctgy

	@Ctgy.setter
	def Ctgy(self, value):
		self._Ctgy = value if value is not None else base_types.UninitialisedField(self, 'Ctgy', Max35Text, False)

	@Ctgy.deleter
	def Ctgy(self):
		del self._Ctgy
		self._Ctgy = base_types.UninitialisedField(self, 'Ctgy', Max35Text, False)

	@property
	def CtgyDtls(self):
		return self._CtgyDtls

	@CtgyDtls.setter
	def CtgyDtls(self, value):
		self._CtgyDtls = value if value is not None else base_types.UninitialisedField(self, 'CtgyDtls', Max35Text, False)

	@CtgyDtls.deleter
	def CtgyDtls(self):
		del self._CtgyDtls
		self._CtgyDtls = base_types.UninitialisedField(self, 'CtgyDtls', Max35Text, False)

	@property
	def DbtrSts(self):
		return self._DbtrSts

	@DbtrSts.setter
	def DbtrSts(self, value):
		self._DbtrSts = value if value is not None else base_types.UninitialisedField(self, 'DbtrSts', Max35Text, False)

	@DbtrSts.deleter
	def DbtrSts(self):
		del self._DbtrSts
		self._DbtrSts = base_types.UninitialisedField(self, 'DbtrSts', Max35Text, False)

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
	def Prd(self):
		return self._Prd

	@Prd.setter
	def Prd(self, value):
		self._Prd = value if value is not None else base_types.UninitialisedField(self, 'Prd', TaxPeriod3, False)

	@Prd.deleter
	def Prd(self):
		del self._Prd
		self._Prd = base_types.UninitialisedField(self, 'Prd', TaxPeriod3, False)

	@property
	def TaxAmt(self):
		return self._TaxAmt

	@TaxAmt.setter
	def TaxAmt(self, value):
		self._TaxAmt = value if value is not None else base_types.UninitialisedField(self, 'TaxAmt', TaxAmount3, False)

	@TaxAmt.deleter
	def TaxAmt(self):
		del self._TaxAmt
		self._TaxAmt = base_types.UninitialisedField(self, 'TaxAmt', TaxAmount3, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CertId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ctgy', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtgyDtls', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrSts', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FrmsCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prd', type=TaxPeriod3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxAmt', type=TaxAmount3, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))