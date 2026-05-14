# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AcquirerProtocolParameters18 import AcquirerProtocolParameters18
from ._ApplicationParameters13 import ApplicationParameters13
from ._HostCommunicationParameter8 import HostCommunicationParameter8
from ._MerchantConfigurationParameters6 import MerchantConfigurationParameters6
from ._PaymentTerminalParameters8 import PaymentTerminalParameters8
from ._SaleToPOIProtocolParameter4 import SaleToPOIProtocolParameter4
from ._SecurityParameters17 import SecurityParameters17
from ._ServiceProviderParameters5 import ServiceProviderParameters5
from ._TMSProtocolParameters8 import TMSProtocolParameters8
from ._TerminalPackageType5 import TerminalPackageType5
from ._TrueFalseIndicator import TrueFalseIndicator

class AcceptorConfigurationContent15(base_types._BaseFieldType):

	__slots__ = ["_AcqrrPrtcolParams", "_ApplParams", "_HstComParams", "_MrchntParams", "_RplcCfgtn", "_SaleToPOIParams", "_SctyParams", "_SvcPrvdrParams", "_TMSPrtcolParams", "_TermnlPackg", "_TermnlParams"]
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
	def ApplParams(self):
		return self._ApplParams

	@ApplParams.setter
	def ApplParams(self, value):
		self._ApplParams = value if type(value) != base_types.auto else self.make_default("ApplParams")

	@ApplParams.deleter
	def ApplParams(self):
		del self._ApplParams
		self._ApplParams = None

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
	def TermnlParams(self):
		return self._TermnlParams

	@TermnlParams.setter
	def TermnlParams(self, value):
		self._TermnlParams = value if type(value) != base_types.auto else self.make_default("TermnlParams")

	@TermnlParams.deleter
	def TermnlParams(self):
		del self._TermnlParams
		self._TermnlParams = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcqrrPrtcolParams', type=AcquirerProtocolParameters18, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ApplParams', type=ApplicationParameters13, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='HstComParams', type=HostCommunicationParameter8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MrchntParams', type=MerchantConfigurationParameters6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RplcCfgtn', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SaleToPOIParams', type=SaleToPOIProtocolParameter4, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SctyParams', type=SecurityParameters17, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcPrvdrParams', type=ServiceProviderParameters5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TMSPrtcolParams', type=TMSProtocolParameters8, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermnlPackg', type=TerminalPackageType5, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TermnlParams', type=PaymentTerminalParameters8, min=0, max=None, mutex_group=None, array=True),
	))