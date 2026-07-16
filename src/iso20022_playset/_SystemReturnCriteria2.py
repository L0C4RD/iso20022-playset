# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class SystemReturnCriteria2(base_types._BaseFieldType):

	__slots__ = ["_AcctIdInd", "_CtryIdInd", "_MmbIdInd", "_SysIdInd"]
	@property
	def AcctIdInd(self):
		return self._AcctIdInd

	@AcctIdInd.setter
	def AcctIdInd(self, value):
		self._AcctIdInd = value if value is not None else base_types.UninitialisedField(self, 'AcctIdInd', RequestedIndicator, False)

	@AcctIdInd.deleter
	def AcctIdInd(self):
		del self._AcctIdInd
		self._AcctIdInd = base_types.UninitialisedField(self, 'AcctIdInd', RequestedIndicator, False)

	@property
	def CtryIdInd(self):
		return self._CtryIdInd

	@CtryIdInd.setter
	def CtryIdInd(self, value):
		self._CtryIdInd = value if value is not None else base_types.UninitialisedField(self, 'CtryIdInd', RequestedIndicator, False)

	@CtryIdInd.deleter
	def CtryIdInd(self):
		del self._CtryIdInd
		self._CtryIdInd = base_types.UninitialisedField(self, 'CtryIdInd', RequestedIndicator, False)

	@property
	def MmbIdInd(self):
		return self._MmbIdInd

	@MmbIdInd.setter
	def MmbIdInd(self, value):
		self._MmbIdInd = value if value is not None else base_types.UninitialisedField(self, 'MmbIdInd', RequestedIndicator, False)

	@MmbIdInd.deleter
	def MmbIdInd(self):
		del self._MmbIdInd
		self._MmbIdInd = base_types.UninitialisedField(self, 'MmbIdInd', RequestedIndicator, False)

	@property
	def SysIdInd(self):
		return self._SysIdInd

	@SysIdInd.setter
	def SysIdInd(self, value):
		self._SysIdInd = value if value is not None else base_types.UninitialisedField(self, 'SysIdInd', RequestedIndicator, False)

	@SysIdInd.deleter
	def SysIdInd(self):
		del self._SysIdInd
		self._SysIdInd = base_types.UninitialisedField(self, 'SysIdInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtryIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SysIdInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))