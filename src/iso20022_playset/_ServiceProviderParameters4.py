from . import base_types
from ._TerminalManagementAction3Code import TerminalManagementAction3Code
from ._GenericIdentification176 import GenericIdentification176
from ._NonFinancialRequestType2Code import NonFinancialRequestType2Code
from ._Max35Text import Max35Text
from ._AcquirerHostConfiguration10 import AcquirerHostConfiguration10
from ._Max256Text import Max256Text

class ServiceProviderParameters4(base_types._BaseFieldType):

	__slots__ = ["_Hst", "_Vrsn", "_ApplId", "_NonFinActnSpprtd", "_SvcPrvdrId", "_ActnTp"]
	@property
	def Hst(self):
		return self._Hst

	@Hst.setter
	def Hst(self, value):
		self._Hst = value if type(value) != base_types.auto else self.make_default("Hst")

	@Hst.deleter
	def Hst(self):
		del self._Hst
		self._Hst = None

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if type(value) != base_types.auto else self.make_default("Vrsn")

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = None

	@property
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if type(value) != base_types.auto else self.make_default("ApplId")

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = None

	@property
	def NonFinActnSpprtd(self):
		return self._NonFinActnSpprtd

	@NonFinActnSpprtd.setter
	def NonFinActnSpprtd(self, value):
		self._NonFinActnSpprtd = value if type(value) != base_types.auto else self.make_default("NonFinActnSpprtd")

	@NonFinActnSpprtd.deleter
	def NonFinActnSpprtd(self):
		del self._NonFinActnSpprtd
		self._NonFinActnSpprtd = None

	@property
	def SvcPrvdrId(self):
		return self._SvcPrvdrId

	@SvcPrvdrId.setter
	def SvcPrvdrId(self, value):
		self._SvcPrvdrId = value if type(value) != base_types.auto else self.make_default("SvcPrvdrId")

	@SvcPrvdrId.deleter
	def SvcPrvdrId(self):
		del self._SvcPrvdrId
		self._SvcPrvdrId = None

	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if type(value) != base_types.auto else self.make_default("ActnTp")

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Hst', type=AcquirerHostConfiguration10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonFinActnSpprtd', type=NonFinancialRequestType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcPrvdrId', type=GenericIdentification176, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
	))

