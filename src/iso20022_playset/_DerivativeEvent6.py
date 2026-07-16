# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DerivativeEventType3Code
from . import EventIdentifier1Choice
from . import TrueFalseIndicator

class DerivativeEvent6(base_types._BaseFieldType):

	__slots__ = ["_AmdmntInd", "_Id", "_TmStmp", "_Tp"]
	@property
	def AmdmntInd(self):
		return self._AmdmntInd

	@AmdmntInd.setter
	def AmdmntInd(self, value):
		self._AmdmntInd = value if value is not None else base_types.UninitialisedField(self, 'AmdmntInd', TrueFalseIndicator, False)

	@AmdmntInd.deleter
	def AmdmntInd(self):
		del self._AmdmntInd
		self._AmdmntInd = base_types.UninitialisedField(self, 'AmdmntInd', TrueFalseIndicator, False)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', EventIdentifier1Choice, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', EventIdentifier1Choice, False)

	@property
	def TmStmp(self):
		return self._TmStmp

	@TmStmp.setter
	def TmStmp(self, value):
		self._TmStmp = value if value is not None else base_types.UninitialisedField(self, 'TmStmp', DateAndDateTime2Choice, False)

	@TmStmp.deleter
	def TmStmp(self):
		del self._TmStmp
		self._TmStmp = base_types.UninitialisedField(self, 'TmStmp', DateAndDateTime2Choice, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', DerivativeEventType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', DerivativeEventType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AmdmntInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=EventIdentifier1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TmStmp', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=DerivativeEventType3Code, min=0, max=1, mutex_group=None, array=False),
	))