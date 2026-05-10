import base_types
import InvestigationStatusReason1Choice
import ExternalInvestigationStatus1Code

class InvestigationStatus2(base_types._BaseFieldType):

	__slots__ = ["_StsRsn", "_Sts"]
	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsRsn', type=InvestigationStatusReason1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=ExternalInvestigationStatus1Code, min=1, max=1, mutex_group=None, array=False),
	))

