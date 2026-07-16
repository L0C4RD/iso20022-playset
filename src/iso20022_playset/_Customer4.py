# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CustomerType2Code
from . import Max35Text
from . import Max70Text
from . import PhoneNumber
from . import TrueFalseIndicator

class Customer4(base_types._BaseFieldType):

	__slots__ = ["_AuthrsdCtctCpny", "_AuthrsdCtctNm", "_AuthrsdCtctPhneNb", "_CstmrRltsh", "_RefNb", "_TaxRegnId", "_Tp", "_VIPInd"]
	@property
	def AuthrsdCtctCpny(self):
		return self._AuthrsdCtctCpny

	@AuthrsdCtctCpny.setter
	def AuthrsdCtctCpny(self, value):
		self._AuthrsdCtctCpny = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdCtctCpny', Max70Text, False)

	@AuthrsdCtctCpny.deleter
	def AuthrsdCtctCpny(self):
		del self._AuthrsdCtctCpny
		self._AuthrsdCtctCpny = base_types.UninitialisedField(self, 'AuthrsdCtctCpny', Max70Text, False)

	@property
	def AuthrsdCtctNm(self):
		return self._AuthrsdCtctNm

	@AuthrsdCtctNm.setter
	def AuthrsdCtctNm(self, value):
		self._AuthrsdCtctNm = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdCtctNm', Max70Text, False)

	@AuthrsdCtctNm.deleter
	def AuthrsdCtctNm(self):
		del self._AuthrsdCtctNm
		self._AuthrsdCtctNm = base_types.UninitialisedField(self, 'AuthrsdCtctNm', Max70Text, False)

	@property
	def AuthrsdCtctPhneNb(self):
		return self._AuthrsdCtctPhneNb

	@AuthrsdCtctPhneNb.setter
	def AuthrsdCtctPhneNb(self, value):
		self._AuthrsdCtctPhneNb = value if value is not None else base_types.UninitialisedField(self, 'AuthrsdCtctPhneNb', PhoneNumber, False)

	@AuthrsdCtctPhneNb.deleter
	def AuthrsdCtctPhneNb(self):
		del self._AuthrsdCtctPhneNb
		self._AuthrsdCtctPhneNb = base_types.UninitialisedField(self, 'AuthrsdCtctPhneNb', PhoneNumber, False)

	@property
	def CstmrRltsh(self):
		return self._CstmrRltsh

	@CstmrRltsh.setter
	def CstmrRltsh(self, value):
		self._CstmrRltsh = value if value is not None else base_types.UninitialisedField(self, 'CstmrRltsh', Max35Text, False)

	@CstmrRltsh.deleter
	def CstmrRltsh(self):
		del self._CstmrRltsh
		self._CstmrRltsh = base_types.UninitialisedField(self, 'CstmrRltsh', Max35Text, False)

	@property
	def RefNb(self):
		return self._RefNb

	@RefNb.setter
	def RefNb(self, value):
		self._RefNb = value if value is not None else base_types.UninitialisedField(self, 'RefNb', Max35Text, False)

	@RefNb.deleter
	def RefNb(self):
		del self._RefNb
		self._RefNb = base_types.UninitialisedField(self, 'RefNb', Max35Text, False)

	@property
	def TaxRegnId(self):
		return self._TaxRegnId

	@TaxRegnId.setter
	def TaxRegnId(self, value):
		self._TaxRegnId = value if value is not None else base_types.UninitialisedField(self, 'TaxRegnId', Max70Text, True)

	@TaxRegnId.deleter
	def TaxRegnId(self):
		del self._TaxRegnId
		self._TaxRegnId = base_types.UninitialisedField(self, 'TaxRegnId', Max70Text, True)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CustomerType2Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CustomerType2Code, False)

	@property
	def VIPInd(self):
		return self._VIPInd

	@VIPInd.setter
	def VIPInd(self, value):
		self._VIPInd = value if value is not None else base_types.UninitialisedField(self, 'VIPInd', TrueFalseIndicator, False)

	@VIPInd.deleter
	def VIPInd(self):
		del self._VIPInd
		self._VIPInd = base_types.UninitialisedField(self, 'VIPInd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AuthrsdCtctCpny', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdCtctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AuthrsdCtctPhneNb', type=PhoneNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrRltsh', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RefNb', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxRegnId', type=Max70Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Tp', type=CustomerType2Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VIPInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))