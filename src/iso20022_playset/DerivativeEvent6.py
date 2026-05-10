from . import base_types
import EventIdentifier1Choice
import DateAndDateTime2Choice
import DerivativeEventType3Code
import TrueFalseIndicator

class DerivativeEvent6(base_types._BaseFieldType):

	__slots__ = ["_TmStmp", "_Id", "_Tp", "_AmdmntInd"]
	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if type(value) != auto else self.make_default("TmStmp")

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if type(value) != auto else self.make_default("Tp")

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = None

	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if type(value) != auto else self.make_default("AmdmntInd")

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TmStmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=EventIdentifier1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DerivativeEventType3Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AmdmntInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))

