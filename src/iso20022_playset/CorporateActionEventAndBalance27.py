import base_types
import SecurityIdentification20
import SupplementaryData1
import CorporateActionBalance51
import EventInformation18

class CorporateActionEventAndBalance27(base_types._BaseFieldType):

	__slots__ = ["_UndrlygScty", "_Bal", "_SplmtryData", "_GnlInf"]
	@property
	def UndrlygScty(self):
		return self._UndrlygScty

	@UndrlygScty.setter
	def UndrlygScty(self, value):
		self._UndrlygScty = value if type(value) != auto else self.make_default("UndrlygScty")

	@UndrlygScty.deleter
	def UndrlygScty(self):
		del self._UndrlygScty
		self._UndrlygScty = None

	@property
	def Bal(self):
		return self._Bal

	@Bal.setter
	def Bal(self, value):
		self._Bal = value if type(value) != auto else self.make_default("Bal")

	@Bal.deleter
	def Bal(self):
		del self._Bal
		self._Bal = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def GnlInf(self):
		return self._GnlInf

	@GnlInf.setter
	def GnlInf(self, value):
		self._GnlInf = value if type(value) != auto else self.make_default("GnlInf")

	@GnlInf.deleter
	def GnlInf(self):
		del self._GnlInf
		self._GnlInf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UndrlygScty', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Bal', type=CorporateActionBalance51, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='GnlInf', type=EventInformation18, min=1, max=1, mutex_group=None, array=False),
	))

