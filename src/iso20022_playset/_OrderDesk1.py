# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import ContactAttributes5
from . import ISODate

class OrderDesk1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_ClsrDts", "_OrdrDsk"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def ClsrDts(self):
		return self._ClsrDts

	@ClsrDts.setter
	def ClsrDts(self, value):
		self._ClsrDts = value if value is not None else base_types.UninitialisedField(self, 'ClsrDts', ISODate, True)

	@ClsrDts.deleter
	def ClsrDts(self):
		del self._ClsrDts
		self._ClsrDts = base_types.UninitialisedField(self, 'ClsrDts', ISODate, True)

	@property
	def OrdrDsk(self):
		return self._OrdrDsk

	@OrdrDsk.setter
	def OrdrDsk(self, value):
		self._OrdrDsk = value if value is not None else base_types.UninitialisedField(self, 'OrdrDsk', ContactAttributes5, False)

	@OrdrDsk.deleter
	def OrdrDsk(self):
		del self._OrdrDsk
		self._OrdrDsk = base_types.UninitialisedField(self, 'OrdrDsk', ContactAttributes5, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ClsrDts', type=ISODate, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrDsk', type=ContactAttributes5, min=0, max=1, mutex_group=None, array=False),
	))