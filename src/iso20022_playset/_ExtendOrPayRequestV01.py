# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExtendOrPayQuery1
from . import PartyAndSignature2

class ExtendOrPayRequestV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_XtndOrPayReqDtls"]
	@property
	def DgtlSgntr(self):
		return self._DgtlSgntr

	@DgtlSgntr.setter
	def DgtlSgntr(self, value):
		self._DgtlSgntr = value if value is not None else base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@DgtlSgntr.deleter
	def DgtlSgntr(self):
		del self._DgtlSgntr
		self._DgtlSgntr = base_types.UninitialisedField(self, 'DgtlSgntr', PartyAndSignature2, False)

	@property
	def XtndOrPayReqDtls(self):
		return self._XtndOrPayReqDtls

	@XtndOrPayReqDtls.setter
	def XtndOrPayReqDtls(self, value):
		self._XtndOrPayReqDtls = value if value is not None else base_types.UninitialisedField(self, 'XtndOrPayReqDtls', ExtendOrPayQuery1, False)

	@XtndOrPayReqDtls.deleter
	def XtndOrPayReqDtls(self):
		del self._XtndOrPayReqDtls
		self._XtndOrPayReqDtls = base_types.UninitialisedField(self, 'XtndOrPayReqDtls', ExtendOrPayQuery1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndOrPayReqDtls', type=ExtendOrPayQuery1, min=1, max=1, mutex_group=None, array=False),
	))