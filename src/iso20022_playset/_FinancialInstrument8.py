# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._DistributionPolicy1Code import DistributionPolicy1Code
from ._FormOfSecurity1Code import FormOfSecurity1Code
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._SecurityIdentification3Choice import SecurityIdentification3Choice
from ._YesNoIndicator import YesNoIndicator

class FinancialInstrument8(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_DnmtnCcy", "_DstrbtnPlcy", "_DualFndInd", "_Id", "_Nm", "_SctiesForm", "_SplmtryId"]
	@property
	def ClssTp(self):
		return self._ClssTp

	@ClssTp.setter
	def ClssTp(self, value):
		self._ClssTp = value if type(value) != base_types.auto else self.make_default("ClssTp")

	@ClssTp.deleter
	def ClssTp(self):
		del self._ClssTp
		self._ClssTp = None

	@property
	def DnmtnCcy(self):
		return self._DnmtnCcy

	@DnmtnCcy.setter
	def DnmtnCcy(self, value):
		self._DnmtnCcy = value if type(value) != base_types.auto else self.make_default("DnmtnCcy")

	@DnmtnCcy.deleter
	def DnmtnCcy(self):
		del self._DnmtnCcy
		self._DnmtnCcy = None

	@property
	def DstrbtnPlcy(self):
		return self._DstrbtnPlcy

	@DstrbtnPlcy.setter
	def DstrbtnPlcy(self, value):
		self._DstrbtnPlcy = value if type(value) != base_types.auto else self.make_default("DstrbtnPlcy")

	@DstrbtnPlcy.deleter
	def DstrbtnPlcy(self):
		del self._DstrbtnPlcy
		self._DstrbtnPlcy = None

	@property
	def DualFndInd(self):
		return self._DualFndInd

	@DualFndInd.setter
	def DualFndInd(self, value):
		self._DualFndInd = value if type(value) != base_types.auto else self.make_default("DualFndInd")

	@DualFndInd.deleter
	def DualFndInd(self):
		del self._DualFndInd
		self._DualFndInd = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def SctiesForm(self):
		return self._SctiesForm

	@SctiesForm.setter
	def SctiesForm(self, value):
		self._SctiesForm = value if type(value) != base_types.auto else self.make_default("SctiesForm")

	@SctiesForm.deleter
	def SctiesForm(self):
		del self._SctiesForm
		self._SctiesForm = None

	@property
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if type(value) != base_types.auto else self.make_default("SplmtryId")

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DnmtnCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DualFndInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification3Choice, min=1, max=10, mutex_group=None, array=True),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))