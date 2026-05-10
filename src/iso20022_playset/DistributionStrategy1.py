from . import base_types
from .DistributionStrategy1Choice import DistributionStrategy1Choice
from .OtherDistributionStrategy1 import OtherDistributionStrategy1

class DistributionStrategy1(base_types._BaseFieldType):

	__slots__ = ["_InvstmtAdvc", "_ExctnWthApprprtnssTstOrNonAdvsdSvcs", "_PrtflMgmt", "_ExctnOnly", "_Othr"]
	@property
	def InvstmtAdvc(self):
		return self._InvstmtAdvc

	@InvstmtAdvc.setter
	def InvstmtAdvc(self, value):
		self._InvstmtAdvc = value if type(value) != auto else self.make_default("InvstmtAdvc")

	@InvstmtAdvc.deleter
	def InvstmtAdvc(self):
		del self._InvstmtAdvc
		self._InvstmtAdvc = None

	@property
	def ExctnWthApprprtnssTstOrNonAdvsdSvcs(self):
		return self._ExctnWthApprprtnssTstOrNonAdvsdSvcs

	@ExctnWthApprprtnssTstOrNonAdvsdSvcs.setter
	def ExctnWthApprprtnssTstOrNonAdvsdSvcs(self, value):
		self._ExctnWthApprprtnssTstOrNonAdvsdSvcs = value if type(value) != auto else self.make_default("ExctnWthApprprtnssTstOrNonAdvsdSvcs")

	@ExctnWthApprprtnssTstOrNonAdvsdSvcs.deleter
	def ExctnWthApprprtnssTstOrNonAdvsdSvcs(self):
		del self._ExctnWthApprprtnssTstOrNonAdvsdSvcs
		self._ExctnWthApprprtnssTstOrNonAdvsdSvcs = None

	@property
	def PrtflMgmt(self):
		return self._PrtflMgmt

	@PrtflMgmt.setter
	def PrtflMgmt(self, value):
		self._PrtflMgmt = value if type(value) != auto else self.make_default("PrtflMgmt")

	@PrtflMgmt.deleter
	def PrtflMgmt(self):
		del self._PrtflMgmt
		self._PrtflMgmt = None

	@property
	def ExctnOnly(self):
		return self._ExctnOnly

	@ExctnOnly.setter
	def ExctnOnly(self, value):
		self._ExctnOnly = value if type(value) != auto else self.make_default("ExctnOnly")

	@ExctnOnly.deleter
	def ExctnOnly(self):
		del self._ExctnOnly
		self._ExctnOnly = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstmtAdvc', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnWthApprprtnssTstOrNonAdvsdSvcs', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrtflMgmt', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ExctnOnly', type=DistributionStrategy1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=OtherDistributionStrategy1, min=0, max=1, mutex_group=None, array=False),
	))

