# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AcquirerHostConfiguration10
from . import GenericIdentification176
from . import Max256Text
from . import Max35Text
from . import NonFinancialRequestType2Code
from . import TerminalManagementAction3Code

class ServiceProviderParameters4(base_types._BaseFieldType):

	__slots__ = ["_ActnTp", "_ApplId", "_Hst", "_NonFinActnSpprtd", "_SvcPrvdrId", "_Vrsn"]
	@property
	def ActnTp(self):
		return self._ActnTp

	@ActnTp.setter
	def ActnTp(self, value):
		self._ActnTp = value if value is not None else base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@ActnTp.deleter
	def ActnTp(self):
		del self._ActnTp
		self._ActnTp = base_types.UninitialisedField(self, 'ActnTp', TerminalManagementAction3Code, False)

	@property
	def ApplId(self):
		return self._ApplId

	@ApplId.setter
	def ApplId(self, value):
		self._ApplId = value if value is not None else base_types.UninitialisedField(self, 'ApplId', Max35Text, True)

	@ApplId.deleter
	def ApplId(self):
		del self._ApplId
		self._ApplId = base_types.UninitialisedField(self, 'ApplId', Max35Text, True)

	@property
	def Hst(self):
		return self._Hst

	@Hst.setter
	def Hst(self, value):
		self._Hst = value if value is not None else base_types.UninitialisedField(self, 'Hst', AcquirerHostConfiguration10, True)

	@Hst.deleter
	def Hst(self):
		del self._Hst
		self._Hst = base_types.UninitialisedField(self, 'Hst', AcquirerHostConfiguration10, True)

	@property
	def NonFinActnSpprtd(self):
		return self._NonFinActnSpprtd

	@NonFinActnSpprtd.setter
	def NonFinActnSpprtd(self, value):
		self._NonFinActnSpprtd = value if value is not None else base_types.UninitialisedField(self, 'NonFinActnSpprtd', NonFinancialRequestType2Code, True)

	@NonFinActnSpprtd.deleter
	def NonFinActnSpprtd(self):
		del self._NonFinActnSpprtd
		self._NonFinActnSpprtd = base_types.UninitialisedField(self, 'NonFinActnSpprtd', NonFinancialRequestType2Code, True)

	@property
	def SvcPrvdrId(self):
		return self._SvcPrvdrId

	@SvcPrvdrId.setter
	def SvcPrvdrId(self, value):
		self._SvcPrvdrId = value if value is not None else base_types.UninitialisedField(self, 'SvcPrvdrId', GenericIdentification176, True)

	@SvcPrvdrId.deleter
	def SvcPrvdrId(self):
		del self._SvcPrvdrId
		self._SvcPrvdrId = base_types.UninitialisedField(self, 'SvcPrvdrId', GenericIdentification176, True)

	@property
	def Vrsn(self):
		return self._Vrsn

	@Vrsn.setter
	def Vrsn(self, value):
		self._Vrsn = value if value is not None else base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	@Vrsn.deleter
	def Vrsn(self):
		del self._Vrsn
		self._Vrsn = base_types.UninitialisedField(self, 'Vrsn', Max256Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActnTp', type=TerminalManagementAction3Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ApplId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Hst', type=AcquirerHostConfiguration10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='NonFinActnSpprtd', type=NonFinancialRequestType2Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SvcPrvdrId', type=GenericIdentification176, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Vrsn', type=Max256Text, min=1, max=1, mutex_group=None, array=False),
	))