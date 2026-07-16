# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcquirerProtocolParameters18
from . import ApplicationParameters13
from . import HostCommunicationParameter8
from . import MerchantConfigurationParameters6
from . import PaymentTerminalParameters8
from . import SaleToPOIProtocolParameter4
from . import SecurityParameters17
from . import ServiceProviderParameters5
from . import TMSProtocolParameters8
from . import TerminalPackageType5
from . import TrueFalseIndicator

class AcceptorConfigurationContent15(base_types._BaseFieldType):

	__slots__ = ["_AcqrrPrtcolParams", "_ApplParams", "_HstComParams", "_MrchntParams", "_RplcCfgtn", "_SaleToPOIParams", "_SctyParams", "_SvcPrvdrParams", "_TMSPrtcolParams", "_TermnlPackg", "_TermnlParams"]
	@property
	def AcqrrPrtcolParams(self):
		return self._AcqrrPrtcolParams

	@AcqrrPrtcolParams.setter
	def AcqrrPrtcolParams(self, value):
		self._AcqrrPrtcolParams = value if value is not None else base_types.UninitialisedField(self, 'AcqrrPrtcolParams', AcquirerProtocolParameters18, True)

	@AcqrrPrtcolParams.deleter
	def AcqrrPrtcolParams(self):
		del self._AcqrrPrtcolParams
		self._AcqrrPrtcolParams = base_types.UninitialisedField(self, 'AcqrrPrtcolParams', AcquirerProtocolParameters18, True)

	@property
	def ApplParams(self):
		return self._ApplParams

	@ApplParams.setter
	def ApplParams(self, value):
		self._ApplParams = value if value is not None else base_types.UninitialisedField(self, 'ApplParams', ApplicationParameters13, True)

	@ApplParams.deleter
	def ApplParams(self):
		del self._ApplParams
		self._ApplParams = base_types.UninitialisedField(self, 'ApplParams', ApplicationParameters13, True)

	@property
	def HstComParams(self):
		return self._HstComParams

	@HstComParams.setter
	def HstComParams(self, value):
		self._HstComParams = value if value is not None else base_types.UninitialisedField(self, 'HstComParams', HostCommunicationParameter8, True)

	@HstComParams.deleter
	def HstComParams(self):
		del self._HstComParams
		self._HstComParams = base_types.UninitialisedField(self, 'HstComParams', HostCommunicationParameter8, True)

	@property
	def MrchntParams(self):
		return self._MrchntParams

	@MrchntParams.setter
	def MrchntParams(self, value):
		self._MrchntParams = value if value is not None else base_types.UninitialisedField(self, 'MrchntParams', MerchantConfigurationParameters6, True)

	@MrchntParams.deleter
	def MrchntParams(self):
		del self._MrchntParams
		self._MrchntParams = base_types.UninitialisedField(self, 'MrchntParams', MerchantConfigurationParameters6, True)

	@property
	def RplcCfgtn(self):
		return self._RplcCfgtn

	@RplcCfgtn.setter
	def RplcCfgtn(self, value):
		self._RplcCfgtn = value if value is not None else base_types.UninitialisedField(self, 'RplcCfgtn', TrueFalseIndicator, False)

	@RplcCfgtn.deleter
	def RplcCfgtn(self):
		del self._RplcCfgtn
		self._RplcCfgtn = base_types.UninitialisedField(self, 'RplcCfgtn', TrueFalseIndicator, False)

	@property
	def SaleToPOIParams(self):
		return self._SaleToPOIParams

	@SaleToPOIParams.setter
	def SaleToPOIParams(self, value):
		self._SaleToPOIParams = value if value is not None else base_types.UninitialisedField(self, 'SaleToPOIParams', SaleToPOIProtocolParameter4, True)

	@SaleToPOIParams.deleter
	def SaleToPOIParams(self):
		del self._SaleToPOIParams
		self._SaleToPOIParams = base_types.UninitialisedField(self, 'SaleToPOIParams', SaleToPOIProtocolParameter4, True)

	@property
	def SctyParams(self):
		return self._SctyParams

	@SctyParams.setter
	def SctyParams(self, value):
		self._SctyParams = value if value is not None else base_types.UninitialisedField(self, 'SctyParams', SecurityParameters17, True)

	@SctyParams.deleter
	def SctyParams(self):
		del self._SctyParams
		self._SctyParams = base_types.UninitialisedField(self, 'SctyParams', SecurityParameters17, True)

	@property
	def SvcPrvdrParams(self):
		return self._SvcPrvdrParams

	@SvcPrvdrParams.setter
	def SvcPrvdrParams(self, value):
		self._SvcPrvdrParams = value if value is not None else base_types.UninitialisedField(self, 'SvcPrvdrParams', ServiceProviderParameters5, True)

	@SvcPrvdrParams.deleter
	def SvcPrvdrParams(self):
		del self._SvcPrvdrParams
		self._SvcPrvdrParams = base_types.UninitialisedField(self, 'SvcPrvdrParams', ServiceProviderParameters5, True)

	@property
	def TMSPrtcolParams(self):
		return self._TMSPrtcolParams

	@TMSPrtcolParams.setter
	def TMSPrtcolParams(self, value):
		self._TMSPrtcolParams = value if value is not None else base_types.UninitialisedField(self, 'TMSPrtcolParams', TMSProtocolParameters8, True)

	@TMSPrtcolParams.deleter
	def TMSPrtcolParams(self):
		del self._TMSPrtcolParams
		self._TMSPrtcolParams = base_types.UninitialisedField(self, 'TMSPrtcolParams', TMSProtocolParameters8, True)

	@property
	def TermnlPackg(self):
		return self._TermnlPackg

	@TermnlPackg.setter
	def TermnlPackg(self, value):
		self._TermnlPackg = value if value is not None else base_types.UninitialisedField(self, 'TermnlPackg', TerminalPackageType5, True)

	@TermnlPackg.deleter
	def TermnlPackg(self):
		del self._TermnlPackg
		self._TermnlPackg = base_types.UninitialisedField(self, 'TermnlPackg', TerminalPackageType5, True)

	@property
	def TermnlParams(self):
		return self._TermnlParams

	@TermnlParams.setter
	def TermnlParams(self, value):
		self._TermnlParams = value if value is not None else base_types.UninitialisedField(self, 'TermnlParams', PaymentTerminalParameters8, True)

	@TermnlParams.deleter
	def TermnlParams(self):
		del self._TermnlParams
		self._TermnlParams = base_types.UninitialisedField(self, 'TermnlParams', PaymentTerminalParameters8, True)

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