# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralType21
from . import ISODate
from . import SecurityIdentification26Choice
from . import TrueFalseIndicator

class CollaterisedData12(base_types._BaseFieldType):

	__slots__ = ["_AsstTp", "_BsktIdr", "_CollValDt", "_NetXpsrCollstnInd"]
	@property
	def AsstTp(self):
		return self._AsstTp

	@AsstTp.setter
	def AsstTp(self, value):
		self._AsstTp = value if value is not None else base_types.UninitialisedField(self, 'AsstTp', CollateralType21, False)

	@AsstTp.deleter
	def AsstTp(self):
		del self._AsstTp
		self._AsstTp = base_types.UninitialisedField(self, 'AsstTp', CollateralType21, False)

	@property
	def BsktIdr(self):
		return self._BsktIdr

	@BsktIdr.setter
	def BsktIdr(self, value):
		self._BsktIdr = value if value is not None else base_types.UninitialisedField(self, 'BsktIdr', SecurityIdentification26Choice, False)

	@BsktIdr.deleter
	def BsktIdr(self):
		del self._BsktIdr
		self._BsktIdr = base_types.UninitialisedField(self, 'BsktIdr', SecurityIdentification26Choice, False)

	@property
	def CollValDt(self):
		return self._CollValDt

	@CollValDt.setter
	def CollValDt(self, value):
		self._CollValDt = value if value is not None else base_types.UninitialisedField(self, 'CollValDt', ISODate, False)

	@CollValDt.deleter
	def CollValDt(self):
		del self._CollValDt
		self._CollValDt = base_types.UninitialisedField(self, 'CollValDt', ISODate, False)

	@property
	def NetXpsrCollstnInd(self):
		return self._NetXpsrCollstnInd

	@NetXpsrCollstnInd.setter
	def NetXpsrCollstnInd(self, value):
		self._NetXpsrCollstnInd = value if value is not None else base_types.UninitialisedField(self, 'NetXpsrCollstnInd', TrueFalseIndicator, False)

	@NetXpsrCollstnInd.deleter
	def NetXpsrCollstnInd(self):
		del self._NetXpsrCollstnInd
		self._NetXpsrCollstnInd = base_types.UninitialisedField(self, 'NetXpsrCollstnInd', TrueFalseIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AsstTp', type=CollateralType21, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BsktIdr', type=SecurityIdentification26Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CollValDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NetXpsrCollstnInd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
	))