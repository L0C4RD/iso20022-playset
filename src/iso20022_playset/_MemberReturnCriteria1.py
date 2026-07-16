# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import RequestedIndicator

class MemberReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_AcctInd", "_ComAdrInd", "_CtctRefInd", "_MmbRtrAdrInd", "_NmInd", "_StsInd", "_TpInd"]
	@property
	def AcctInd(self):
		return self._AcctInd

	@AcctInd.setter
	def AcctInd(self, value):
		self._AcctInd = value if value is not None else base_types.UninitialisedField(self, 'AcctInd', RequestedIndicator, False)

	@AcctInd.deleter
	def AcctInd(self):
		del self._AcctInd
		self._AcctInd = base_types.UninitialisedField(self, 'AcctInd', RequestedIndicator, False)

	@property
	def ComAdrInd(self):
		return self._ComAdrInd

	@ComAdrInd.setter
	def ComAdrInd(self, value):
		self._ComAdrInd = value if value is not None else base_types.UninitialisedField(self, 'ComAdrInd', RequestedIndicator, False)

	@ComAdrInd.deleter
	def ComAdrInd(self):
		del self._ComAdrInd
		self._ComAdrInd = base_types.UninitialisedField(self, 'ComAdrInd', RequestedIndicator, False)

	@property
	def CtctRefInd(self):
		return self._CtctRefInd

	@CtctRefInd.setter
	def CtctRefInd(self, value):
		self._CtctRefInd = value if value is not None else base_types.UninitialisedField(self, 'CtctRefInd', RequestedIndicator, False)

	@CtctRefInd.deleter
	def CtctRefInd(self):
		del self._CtctRefInd
		self._CtctRefInd = base_types.UninitialisedField(self, 'CtctRefInd', RequestedIndicator, False)

	@property
	def MmbRtrAdrInd(self):
		return self._MmbRtrAdrInd

	@MmbRtrAdrInd.setter
	def MmbRtrAdrInd(self, value):
		self._MmbRtrAdrInd = value if value is not None else base_types.UninitialisedField(self, 'MmbRtrAdrInd', RequestedIndicator, False)

	@MmbRtrAdrInd.deleter
	def MmbRtrAdrInd(self):
		del self._MmbRtrAdrInd
		self._MmbRtrAdrInd = base_types.UninitialisedField(self, 'MmbRtrAdrInd', RequestedIndicator, False)

	@property
	def NmInd(self):
		return self._NmInd

	@NmInd.setter
	def NmInd(self, value):
		self._NmInd = value if value is not None else base_types.UninitialisedField(self, 'NmInd', RequestedIndicator, False)

	@NmInd.deleter
	def NmInd(self):
		del self._NmInd
		self._NmInd = base_types.UninitialisedField(self, 'NmInd', RequestedIndicator, False)

	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if value is not None else base_types.UninitialisedField(self, 'StsInd', RequestedIndicator, False)

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = base_types.UninitialisedField(self, 'StsInd', RequestedIndicator, False)

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if value is not None else base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = base_types.UninitialisedField(self, 'TpInd', RequestedIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComAdrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CtctRefInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbRtrAdrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))