# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GDPRDataConsent1Choice
from . import ISODate
from . import YesNoIndicator

class GDPRData1(base_types._BaseFieldType):

	__slots__ = ["_CnsntDt", "_CnsntInd", "_CnsntTp"]
	@property
	def CnsntDt(self):
		return self._CnsntDt

	@CnsntDt.setter
	def CnsntDt(self, value):
		self._CnsntDt = value if value is not None else base_types.UninitialisedField(self, 'CnsntDt', ISODate, False)

	@CnsntDt.deleter
	def CnsntDt(self):
		del self._CnsntDt
		self._CnsntDt = base_types.UninitialisedField(self, 'CnsntDt', ISODate, False)

	@property
	def CnsntInd(self):
		return self._CnsntInd

	@CnsntInd.setter
	def CnsntInd(self, value):
		self._CnsntInd = value if value is not None else base_types.UninitialisedField(self, 'CnsntInd', YesNoIndicator, False)

	@CnsntInd.deleter
	def CnsntInd(self):
		del self._CnsntInd
		self._CnsntInd = base_types.UninitialisedField(self, 'CnsntInd', YesNoIndicator, False)

	@property
	def CnsntTp(self):
		return self._CnsntTp

	@CnsntTp.setter
	def CnsntTp(self, value):
		self._CnsntTp = value if value is not None else base_types.UninitialisedField(self, 'CnsntTp', GDPRDataConsent1Choice, False)

	@CnsntTp.deleter
	def CnsntTp(self):
		del self._CnsntTp
		self._CnsntTp = base_types.UninitialisedField(self, 'CnsntTp', GDPRDataConsent1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnsntDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CnsntTp', type=GDPRDataConsent1Choice, min=1, max=1, mutex_group=None, array=False),
	))