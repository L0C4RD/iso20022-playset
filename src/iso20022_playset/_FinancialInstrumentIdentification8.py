# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ClassificationType32Choice import ClassificationType32Choice
from ._FinancialInstrumentIdentification9 import FinancialInstrumentIdentification9
from ._Max350Text import Max350Text
from ._Max35Text import Max35Text
from ._SecurityIdentification46Choice import SecurityIdentification46Choice
from ._YesNoIndicator import YesNoIndicator

class FinancialInstrumentIdentification8(base_types._BaseFieldType):

	__slots__ = ["_AltrnScty", "_ClssfctnTp", "_Id", "_Nm", "_RstrctdInd", "_ShrtNm"]
	@property
	def AltrnScty(self):
		return self._AltrnScty

	@AltrnScty.setter
	def AltrnScty(self, value):
		self._AltrnScty = value if type(value) != base_types.auto else self.make_default("AltrnScty")

	@AltrnScty.deleter
	def AltrnScty(self):
		del self._AltrnScty
		self._AltrnScty = None

	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Nm(self):
		return self._Nm

	@Nm.setter
	def Nm(self, value):
		self._Nm = value if type(value) != base_types.auto else self.make_default("Nm")

	@Nm.deleter
	def Nm(self):
		del self._Nm
		self._Nm = None

	@property
	def RstrctdInd(self):
		return self._RstrctdInd

	@RstrctdInd.setter
	def RstrctdInd(self, value):
		self._RstrctdInd = value if type(value) != base_types.auto else self.make_default("RstrctdInd")

	@RstrctdInd.deleter
	def RstrctdInd(self):
		del self._RstrctdInd
		self._RstrctdInd = None

	@property
	def ShrtNm(self):
		return self._ShrtNm

	@ShrtNm.setter
	def ShrtNm(self, value):
		self._ShrtNm = value if type(value) != base_types.auto else self.make_default("ShrtNm")

	@ShrtNm.deleter
	def ShrtNm(self):
		del self._ShrtNm
		self._ShrtNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AltrnScty', type=FinancialInstrumentIdentification9, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType32Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Id', type=SecurityIdentification46Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Nm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RstrctdInd', type=YesNoIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ShrtNm', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))