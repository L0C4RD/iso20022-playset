from . import base_types
from .Max350Text import Max350Text
from .YesNoIndicator import YesNoIndicator
from .DeMinimus1Choice import DeMinimus1Choice

class NewIssueAllocation2(base_types._BaseFieldType):

	__slots__ = ["_Rstrctd", "_DeMnms", "_XmptPrsnRsn"]
	@property
	def Rstrctd(self):
		return self._Rstrctd

	@Rstrctd.setter
	def Rstrctd(self, value):
		self._Rstrctd = value if type(value) != base_types.auto else self.make_default("Rstrctd")

	@Rstrctd.deleter
	def Rstrctd(self):
		del self._Rstrctd
		self._Rstrctd = None

	@property
	def DeMnms(self):
		return self._DeMnms

	@DeMnms.setter
	def DeMnms(self, value):
		self._DeMnms = value if type(value) != base_types.auto else self.make_default("DeMnms")

	@DeMnms.deleter
	def DeMnms(self):
		del self._DeMnms
		self._DeMnms = None

	@property
	def XmptPrsnRsn(self):
		return self._XmptPrsnRsn

	@XmptPrsnRsn.setter
	def XmptPrsnRsn(self, value):
		self._XmptPrsnRsn = value if type(value) != base_types.auto else self.make_default("XmptPrsnRsn")

	@XmptPrsnRsn.deleter
	def XmptPrsnRsn(self):
		del self._XmptPrsnRsn
		self._XmptPrsnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Rstrctd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DeMnms', type=DeMinimus1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XmptPrsnRsn', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

