from . import base_types
from .Max350Text import Max350Text
from .SecurityIdentification25Choice import SecurityIdentification25Choice
from .DistributionPolicy1Code import DistributionPolicy1Code
from .FormOfSecurity1Code import FormOfSecurity1Code
from .YesNoIndicator import YesNoIndicator
from .Max35Text import Max35Text

class FinancialInstrument88(base_types._BaseFieldType):

	__slots__ = ["_ClssTp", "_Id", "_ShrtNm", "_SctiesForm", "_Nm", "_SplmtryId", "_DstrbtnPlcy", "_DmtrlsdInd"]
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
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != base_types.auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

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
	def SplmtryId(self):
		return self._SplmtryId

	@SplmtryId.setter
	def SplmtryId(self, value):
		self._SplmtryId = value if type(value) != base_types.auto else self.make_default("SplmtryId")

	@SplmtryId.deleter
	def SplmtryId(self):
		del self._SplmtryId
		self._SplmtryId = None

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
	def DmtrlsdInd(self):
		return self._DmtrlsdInd

	@DmtrlsdInd.setter
	def DmtrlsdInd(self, value):
		self._DmtrlsdInd = value if type(value) != base_types.auto else self.make_default("DmtrlsdInd")

	@DmtrlsdInd.deleter
	def DmtrlsdInd(self):
		del self._DmtrlsdInd
		self._DmtrlsdInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification25Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesForm', type=FormOfSecurity1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DstrbtnPlcy', type=DistributionPolicy1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DmtrlsdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
	))

