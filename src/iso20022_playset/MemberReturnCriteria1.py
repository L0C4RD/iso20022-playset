import base_types
import RequestedIndicator

class MemberReturnCriteria1(base_types._BaseFieldType):

	__slots__ = ["_CtctRefInd", "_StsInd", "_AcctInd", "_NmInd", "_MmbRtrAdrInd", "_TpInd", "_ComAdrInd"]
	@property
	def CtctRefInd(self):
		return self._CtctRefInd

	@CtctRefInd.setter
	def CtctRefInd(self, value):
		self._CtctRefInd = value if type(value) != auto else self.make_default("CtctRefInd")

	@CtctRefInd.deleter
	def CtctRefInd(self):
		del self._CtctRefInd
		self._CtctRefInd = None

	@property
	def StsInd(self):
		return self._StsInd

	@StsInd.setter
	def StsInd(self, value):
		self._StsInd = value if type(value) != auto else self.make_default("StsInd")

	@StsInd.deleter
	def StsInd(self):
		del self._StsInd
		self._StsInd = None

	@property
	def AcctInd(self):
		return self._AcctInd

	@AcctInd.setter
	def AcctInd(self, value):
		self._AcctInd = value if type(value) != auto else self.make_default("AcctInd")

	@AcctInd.deleter
	def AcctInd(self):
		del self._AcctInd
		self._AcctInd = None

	@property
	def NmInd(self):
		return self._NmInd

	@NmInd.setter
	def NmInd(self, value):
		self._NmInd = value if type(value) != auto else self.make_default("NmInd")

	@NmInd.deleter
	def NmInd(self):
		del self._NmInd
		self._NmInd = None

	@property
	def MmbRtrAdrInd(self):
		return self._MmbRtrAdrInd

	@MmbRtrAdrInd.setter
	def MmbRtrAdrInd(self, value):
		self._MmbRtrAdrInd = value if type(value) != auto else self.make_default("MmbRtrAdrInd")

	@MmbRtrAdrInd.deleter
	def MmbRtrAdrInd(self):
		del self._MmbRtrAdrInd
		self._MmbRtrAdrInd = None

	@property
	def TpInd(self):
		return self._TpInd

	@TpInd.setter
	def TpInd(self, value):
		self._TpInd = value if type(value) != auto else self.make_default("TpInd")

	@TpInd.deleter
	def TpInd(self):
		del self._TpInd
		self._TpInd = None

	@property
	def ComAdrInd(self):
		return self._ComAdrInd

	@ComAdrInd.setter
	def ComAdrInd(self, value):
		self._ComAdrInd = value if type(value) != auto else self.make_default("ComAdrInd")

	@ComAdrInd.deleter
	def ComAdrInd(self):
		del self._ComAdrInd
		self._ComAdrInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtctRefInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AcctInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NmInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MmbRtrAdrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TpInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ComAdrInd', type=RequestedIndicator, min=0, max=1, mutex_group=None, array=False),
	))

