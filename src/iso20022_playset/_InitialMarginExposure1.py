# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount3
from . import MarginType2Choice
from . import TrueFalseIndicator

class InitialMarginExposure1(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_CoreInd", "_Tp"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if value is not None else base_types.UninitialisedField(self, 'Amt', Amount3, False)

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = base_types.UninitialisedField(self, 'Amt', Amount3, False)

	@property
	def CoreInd(self):
		return self._CoreInd

	@CoreInd.setter
	def CoreInd(self, value):
		self._CoreInd = value if value is not None else base_types.UninitialisedField(self, 'CoreInd', TrueFalseIndicator, False)

	@CoreInd.deleter
	def CoreInd(self):
		del self._CoreInd
		self._CoreInd = base_types.UninitialisedField(self, 'CoreInd', TrueFalseIndicator, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', MarginType2Choice, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', MarginType2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=Amount3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CoreInd', type=TrueFalseIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=MarginType2Choice, min=1, max=1, mutex_group=None, array=False),
	))