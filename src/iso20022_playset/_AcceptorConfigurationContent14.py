from . import base_types
from ._ServiceProviderParameters4 import ServiceProviderParameters4
from ._MerchantConfigurationParameters6 import MerchantConfigurationParameters6
from ._HostCommunicationParameter7 import HostCommunicationParameter7
from ._ApplicationParameters13 import ApplicationParameters13
from ._TerminalPackageType5 import TerminalPackageType5
from ._SaleToPOIProtocolParameter3 import SaleToPOIProtocolParameter3
from ._PaymentTerminalParameters8 import PaymentTerminalParameters8
from ._AcquirerProtocolParameters17 import AcquirerProtocolParameters17
from ._TrueFalseIndicator import TrueFalseIndicator
from ._SecurityParameters16 import SecurityParameters16
from ._TMSProtocolParameters7 import TMSProtocolParameters7

class AcceptorConfigurationContent14(base_types._BaseFieldType):

	__slots__ = ["_TermnlPackg", "_AcqrrPrtcolParams", "_HstComParams", "_TermnlParams", "_MrchntParams", "_RplcCfgtn", "_TMSPrtcolParams", "_SctyParams", "_SvcPrvdrParams", "_SaleToPOIParams", "_ApplParams"]
	@property
	def TermnlPackg(self):
		return self._TermnlPackg

	@TermnlPackg.setter
	def TermnlPackg(self, value):
		self._TermnlPackg = value if type(value) != base_types.auto else self.make_default("TermnlPackg")

	@TermnlPackg.deleter
	def TermnlPackg(self):
		del self._TermnlPackg
		self._TermnlPackg = None

	@property
	def AcqrrPrtcolParams(self):
		return self._AcqrrPrtcolParams

	@AcqrrPrtcolParams.setter
	def AcqrrPrtcolParams(self, value):
		self._AcqrrPrtcolParams = value if type(value) != base_types.auto else self.make_default("AcqrrPrtcolParams")

	@AcqrrPrtcolParams.deleter
	def AcqrrPrtcolParams(self):
		del self._AcqrrPrtcolParams
		self._AcqrrPrtcolParams = None

	@property
	def HstComParams(self):
		return self._HstComParams

	@HstComParams.setter
	def HstComParams(self, value):
		self._HstComParams = value if type(value) != base_types.auto else self.make_default("HstComParams")

	@HstComParams.deleter
	def HstComParams(self):
		del self._HstComParams
		self._HstComParams = None

	@property
	def TermnlParams(self):
		return self._TermnlParams

	@TermnlParams.setter
	def TermnlParams(self, value):
		self._TermnlParams = value if type(value) != base_types.auto else self.make_default("TermnlParams")

	@TermnlParams.deleter
	def TermnlParams(self):
		del self._TermnlParams
		self._TermnlParams = None

	@property
	def MrchntParams(self):
		return self._MrchntParams

	@MrchntParams.setter
	def MrchntParams(self, value):
		self._MrchntParams = value if type(value) != base_types.auto else self.make_default("MrchntParams")

	@MrchntParams.deleter
	def MrchntParams(self):
		del self._MrchntParams
		self._MrchntParams = None

	@property
	def RplcCfgtn(self):
		return self._RplcCfgtn

	@RplcCfgtn.setter
	def RplcCfgtn(self, value):
		self._RplcCfgtn = value if type(value) != base_types.auto else self.make_default("RplcCfgtn")

	@RplcCfgtn.deleter
	def RplcCfgtn(self):
		del self._RplcCfgtn
		self._RplcCfgtn = None

	@property
	def TMSPrtcolParams(self):
		return self._TMSPrtcolParams

	@TMSPrtcolParams.setter
	def TMSPrtcolParams(self, value):
		self._TMSPrtcolParams = value if type(value) != base_types.auto else self.make_default("TMSPrtcolParams")

	@TMSPrtcolParams.deleter
	def TMSPrtcolParams(self):
		del self._TMSPrtcolParams
		self._TMSPrtcolParams = None

	@property
	def SctyParams(self):
		return self._SctyParams

	@SctyParams.setter
	def SctyParams(self, value):
		self._SctyParams = value if type(value) != base_types.auto else self.make_default("SctyParams")

	@SctyParams.deleter
	def SctyParams(self):
		del self._SctyParams
		self._SctyParams = None

	@property
	def SvcPrvdrParams(self):
		return self._SvcPrvdrParams

	@SvcPrvdrParams.setter
	def SvcPrvdrParams(self, value):
		self._SvcPrvdrParams = value if type(value) != base_types.auto else self.make_default("SvcPrvdrParams")

	@SvcPrvdrParams.deleter
	def SvcPrvdrParams(self):
		del self._SvcPrvdrParams
		self._SvcPrvdrParams = None

	@property
	def SaleToPOIParams(self):
		return self._SaleToPOIParams

	@SaleToPOIParams.setter
	def SaleToPOIParams(self, value):
		self._SaleToPOIParams = value if type(value) != base_types.auto else self.make_default("SaleToPOIParams")

	@SaleToPOIParams.deleter
	def SaleToPOIParams(self):
		del self._SaleToPOIParams
		self._SaleToPOIParams = None

	@property
	def ApplParams(self):
		return self._ApplParams

	@ApplParams.setter
	def ApplParams(self, value):
		self._ApplParams = value if type(value) != base_types.auto else self.make_default("ApplParams")

	@ApplParams.deleter
	def ApplParams(self):
		del self._ApplParams
		self._ApplParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TermnlPackg', type=TerminalPackageType5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='AcqrrPrtcolParams', type=AcquirerProtocolParameters17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstComParams', type=HostCommunicationParameter7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermnlParams', type=PaymentTerminalParameters8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrchntParams', type=MerchantConfigurationParameters6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RplcCfgtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSPrtcolParams', type=TMSProtocolParameters7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyParams', type=SecurityParameters16, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcPrvdrParams', type=ServiceProviderParameters4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SaleToPOIParams', type=SaleToPOIProtocolParameter3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplParams', type=ApplicationParameters13, min=0, max=None, mutex_group=None, array=True),
	))

