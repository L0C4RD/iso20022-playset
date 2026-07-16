# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ExtendOrPayQuery2
from . import PartyAndSignature2

class ExtendOrPayResponseV01(base_types._BaseFieldType):

	__slots__ = ["_DgtlSgntr", "_XtndOrPayRspnDtls"]
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
	def XtndOrPayRspnDtls(self):
		return self._XtndOrPayRspnDtls

	@XtndOrPayRspnDtls.setter
	def XtndOrPayRspnDtls(self, value):
		self._XtndOrPayRspnDtls = value if value is not None else base_types.UninitialisedField(self, 'XtndOrPayRspnDtls', ExtendOrPayQuery2, False)

	@XtndOrPayRspnDtls.deleter
	def XtndOrPayRspnDtls(self):
		del self._XtndOrPayRspnDtls
		self._XtndOrPayRspnDtls = base_types.UninitialisedField(self, 'XtndOrPayRspnDtls', ExtendOrPayQuery2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DgtlSgntr', type=PartyAndSignature2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtndOrPayRspnDtls', type=ExtendOrPayQuery2, min=1, max=1, mutex_group=None, array=False),
	))