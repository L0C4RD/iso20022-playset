# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdjustmentRequest1
from . import CompensationRequest1
from . import DebitAuthorisation3
from . import Max500Text

class AdditionalRequestData1Choice(base_types._BaseFieldType):

	__slots__ = ["_ReqNrrtv", "_ReqdCompstn", "_ReqdDbtAuthstn", "_ReqdValtn"]
	@property
	def ReqNrrtv(self):
		return self._ReqNrrtv

	@ReqNrrtv.setter
	def ReqNrrtv(self, value):
		self._ReqNrrtv = value if value is not None else base_types.UninitialisedField(self, 'ReqNrrtv', Max500Text, False)

	@ReqNrrtv.deleter
	def ReqNrrtv(self):
		del self._ReqNrrtv
		self._ReqNrrtv = base_types.UninitialisedField(self, 'ReqNrrtv', Max500Text, False)

	@property
	def ReqdCompstn(self):
		return self._ReqdCompstn

	@ReqdCompstn.setter
	def ReqdCompstn(self, value):
		self._ReqdCompstn = value if value is not None else base_types.UninitialisedField(self, 'ReqdCompstn', CompensationRequest1, False)

	@ReqdCompstn.deleter
	def ReqdCompstn(self):
		del self._ReqdCompstn
		self._ReqdCompstn = base_types.UninitialisedField(self, 'ReqdCompstn', CompensationRequest1, False)

	@property
	def ReqdDbtAuthstn(self):
		return self._ReqdDbtAuthstn

	@ReqdDbtAuthstn.setter
	def ReqdDbtAuthstn(self, value):
		self._ReqdDbtAuthstn = value if value is not None else base_types.UninitialisedField(self, 'ReqdDbtAuthstn', DebitAuthorisation3, False)

	@ReqdDbtAuthstn.deleter
	def ReqdDbtAuthstn(self):
		del self._ReqdDbtAuthstn
		self._ReqdDbtAuthstn = base_types.UninitialisedField(self, 'ReqdDbtAuthstn', DebitAuthorisation3, False)

	@property
	def ReqdValtn(self):
		return self._ReqdValtn

	@ReqdValtn.setter
	def ReqdValtn(self, value):
		self._ReqdValtn = value if value is not None else base_types.UninitialisedField(self, 'ReqdValtn', AdjustmentRequest1, False)

	@ReqdValtn.deleter
	def ReqdValtn(self):
		del self._ReqdValtn
		self._ReqdValtn = base_types.UninitialisedField(self, 'ReqdValtn', AdjustmentRequest1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ReqNrrtv', type=Max500Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqdCompstn', type=CompensationRequest1, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqdDbtAuthstn', type=DebitAuthorisation3, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ReqdValtn', type=AdjustmentRequest1, min=0, max=1, mutex_group=1, array=False),
	))